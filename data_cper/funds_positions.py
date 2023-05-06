import datetime
import pandas as pd
import numpy as np
import akshare as ak
import os
import sys
import talib
import configparser
import time
import requests

sys.path.append('..')
os.chdir(os.path.dirname(__file__))
from common.smooth_tool import min_max_dist_pd
from common.trade_date import get_next_weekday, get_trade_day, get_delta_trade_day


def get_funds_postions() -> pd.DataFrame:
    ''' 获取公募基金[股票型、混合平衡型、灵活配置型]仓位，每周更新 '''
    gp_pos = ak.fund_stock_position_lg()
    bal_pos = ak.fund_balance_position_lg()
    smt_pos = ak.fund_linghuo_position_lg()
    funds_pos = pd.DataFrame({'gp': gp_pos['position'].values,
                              'bal': bal_pos['position'].values,
                              'smt': smt_pos['position'].values},
                             index=gp_pos['date'])
    return funds_pos


def get_funds_rate(funds_pos: pd.DataFrame, windows=150) -> pd.DataFrame:
    ''' 公募基金仓位高低分位 (长期-150周) '''
    return min_max_dist_pd(funds_pos, windows=windows)


def get_hsgt_acc_flow():
    ''' 北向累计净流入、累计净买入资金量: 东财数据 '''
    north_acc_flow = ak.stock_hsgt_north_acc_flow_in_em('北上')
    north_acc_flow.set_index('date', inplace=True)
    north_acc_flow /= 1e4
    sh_acc_flow = ak.stock_hsgt_hist_em('沪股通').set_index('日期')
    sz_acc_flow = ak.stock_hsgt_hist_em('深股通').set_index('日期')
    # 2020-10-13 数据空缺
    north_pad_flow = sh_acc_flow['历史累计净买额'].add(
        sz_acc_flow['历史累计净买额'], fill_value=0)
    north_pad_flow.index = [d.strftime('%Y-%m-%d')
                            for d in north_pad_flow.index]
    north_pad_flow.index.name = 'date'
    north_acc_flow.columns = ['inflow']
    north_acc_flow['purchase'] = north_pad_flow
    north_acc_flow.fillna(method='ffill', inplace=True)
    return north_acc_flow


def get_north_flow_bias(north_flow: pd.DataFrame, N=20, window=120, ma_type='ma'):
    ''' 北向流入资金偏离度及其分位数 '''
    north_name = north_flow.columns
    ma_fun_dic = {'ma': talib.MA, 'ema': talib.EMA}
    ma_fun = ma_fun_dic.get(ma_type, talib.MA)
    for i in range(north_flow.shape[1]):
        north_flow[north_name[i]+'_bias'] = north_flow.iloc[:, i] / \
            ma_fun(north_flow.iloc[:, i], N)*100-100
        north_flow[north_name[i]+'_brate'] = min_max_dist_pd(
            north_flow, window, north_name[i]+'_bias')
    return north_flow


def _market_margin_hist(market: int = 1) -> pd.DataFrame:
    """
    金十数据, 上海（深圳）融资融券报告, 数据区间从20100331-至今
    https://datacenter.jin10.com/reportType/dc_market_margin_sse(sz)
    :return: pandas.DataFrame
    """
    t = time.time()
    params = {"_": t}
    res = requests.get(
        f"https://cdn.jin10.com/data_center/reports/fs_{market}.json", params=params
    )
    json_data = res.json()
    temp_df = pd.DataFrame(json_data["values"]).T
    temp_df.columns = ["融资买入额", "融资余额", "融券卖出量", "融券余量", "融券余额", "融资融券余额"]
    temp_df.sort_index(inplace=True)
    temp_df.index = pd.to_datetime(temp_df.index)
    temp_df = temp_df.astype("float")
    return temp_df


def _szse_daily_sumamry(end_date='20230408'):
    dlst = ak.tool_trade_date_hist_sina()['trade_date']
    dlst = [d.strftime('%Y%m%d') for d in dlst]
    dlst = [d for d in dlst if d>=end_date and d<='20230413']
    res = dict()
    for d in dlst[::-1]:
        time.sleep(0.8)
        print('>>', d)
        try:
            amt_pd = ak.stock_szse_summary(d)
            amt_arr = amt_pd.loc[amt_pd['证券类别'].apply(
                lambda x: x in ('主板A股', '主板B股', '中小板','创业板','创业板A股')), '成交金额'].values
            res[d] = np.insert(amt_arr,2,np.nan) if amt_arr.size == 3 else amt_arr
        except:
            print('<<',d,'wrong.')
            return res
    return res

def _szse_daily_mar(start_date='20200820', end_date='20230413'):
    dlst = ak.tool_trade_date_hist_sina()['trade_date']
    dlst = [d.strftime('%Y%m%d') for d in dlst]
    dlst = [d for d in dlst if d>=start_date and d<=end_date]
    amt_arr = None
    for d in dlst:
        time.sleep(0.8)
        print('>>', d)
        try:
            namt_arr = ak.stock_margin_szse(d).values
            # namt_arr = np.append(namt_arr,d)
            amt_arr = np.r_[amt_arr, namt_arr] if amt_arr is not None else namt_arr
        except Exception as e:
            print(e)
            # print('<<',d,'wrong.')
            return amt_arr
    return amt_arr

def margin_amount_sh(date: str):
    ''' 上海融资融券及成交情况 '''
    old_d = get_delta_trade_day(date, -1).strftime('%Y%m%d')
    # 两融情况
    mrg_pd = ak.stock_margin_sse(
        start_date=old_d, end_date=date.replace('-', ''))
    mrg_n_fs, mrg_n_p = mrg_pd.loc[0, '融资余额'], mrg_pd.loc[0, '融资买入额']
    mrg_o_fs = mrg_pd.loc[1, '融资余额']
    mrg_n_qyl, mrg_n_qol = mrg_pd.loc[0, '融券余量'], mrg_pd.loc[0, '融券卖出量']
    mrg_o_qyl = mrg_pd.loc[1, '融券余量']
    mrg_n_qyle = mrg_pd.loc[0, '融券余量金额']
    mrg_n_zqye = mrg_pd.loc[0, '融资融券余额']
    mrg_n_jp = mrg_n_fs - mrg_o_fs      # 净买入
    mrg_n_q = mrg_n_p-mrg_n_jp          # 偿还
    mrg_n_jqol = mrg_n_qyl - mrg_o_qyl  # 净卖出
    mrg_n_qchl = mrg_n_qol-mrg_n_jqol   # 偿还量
    mrg_n_zmqe = mrg_n_fs - mrg_n_qyle  # 融资-融券
    mrg_arr = np.array([[mrg_n_fs, mrg_n_p, mrg_n_q, mrg_n_jp, mrg_n_qyle,
                       mrg_n_qyl, mrg_n_qol, mrg_n_qchl, mrg_n_jqol, mrg_n_zqye, mrg_n_zmqe]])
    # 成交情况
    amt_pd = ak.stock_sse_deal_daily(date.replace('-', ''))
    amt_pd = amt_pd.loc[amt_pd['单日情况'] == '成交金额', ['主板A', '主板B', '科创板']]
    con_arr = np.hstack((mrg_arr, (amt_pd.values*1e8).round(1)))
    con_pd = pd.DataFrame(con_arr, columns=('融资余额', '融资买入额', '融资偿还额', '融资净买入', '融券余额', '融券余量',
                          '融券卖出量', '融券偿还量', '融券净卖出', '两融总额', '两融差额', 'A股成交额', 'B股成交额', '科创板成交额'), index=[date])
    return con_pd


def margin_amount_sz(date: str):
    ''' 深圳融资融券及成交情况 '''
    old_d = get_delta_trade_day(date, -1).strftime('%Y%m%d')
    date_ = date.replace('-', '')
    # 两融情况
    mrg_macro = ak.macro_china_market_margin_sz()
    mrg_macro.rename(lambda x:x.strftime('%Y%m%d'),axis=0,inplace=True)
    mrg_pd = ak.stock_margin_szse(date_)*1e8
    mrg_opd = ak.stock_margin_szse(old_d)*1e8
    # 此处混合使用两方数据
    mrg_n_fs = mrg_macro.loc[date_, '融资余额']
    mrg_n_p = mrg_macro.loc[date_, '融资买入额']
    mrg_o_fs = mrg_macro.loc[old_d, '融资余额']
    mrg_n_qyl = round(mrg_pd.loc[0, '融券余量'],1)
    mrg_n_qol = round(mrg_pd.loc[0, '融券卖出量'],1)
    mrg_o_qyl = round(mrg_opd.loc[0, '融券余量'],1)
    mrg_n_qyle = mrg_macro.loc[date_, '融券余额']
    mrg_n_zqye = mrg_macro.loc[date_, '融资融券余额']
    mrg_n_jp = mrg_n_fs - mrg_o_fs      # 净买入
    mrg_n_q = mrg_n_p-mrg_n_jp          # 偿还
    mrg_n_jqol = mrg_n_qyl - mrg_o_qyl  # 净卖出
    mrg_n_qchl = mrg_n_qol-mrg_n_jqol   # 偿还量
    mrg_n_zmqe = mrg_n_fs - mrg_n_qyle  # 融资-融券
    mrg_arr = np.array([mrg_n_fs, mrg_n_p, mrg_n_q, mrg_n_jp, mrg_n_qyle,
                       mrg_n_qyl, mrg_n_qol, mrg_n_qchl, mrg_n_jqol, mrg_n_zqye, mrg_n_zmqe])
    # 成交情况
    amt_pd = ak.stock_szse_summary(date_)
    amt_arr = amt_pd.loc[amt_pd['证券类别'].apply(
        lambda x: x in ('主板A股', '主板B股', '中小板', '创业板', '创业板A股')), '成交金额'].values
    amt_arr = np.insert(amt_arr, 2, np.nan) if amt_arr.size == 3 else amt_arr
    con_arr = np.hstack((mrg_arr, amt_arr))
    con_pd = pd.DataFrame([con_arr], columns=('融资余额', '融资买入额',
                            '融资偿还额', '融资净买入', '融券余额', '融券余量',
                            '融券卖出量', '融券偿还量', '融券净卖出', '两融总额',
                            '两融差额', 'A股成交额', 'B股成交额', '中小板成交额',
                            '创业板成交额'), index=[date])
    return con_pd

def append_margin_file(market='sh', cfg_file=''):
    ''' 添加两市融资数据 '''
    if not cfg_file:
        cfg_file = '../trade.ini'
    if market.lower() not in ('sh', 'sz'):
        return
    cfg_sec = 'Margin_{}'.format(market.upper())
    mrg_pd_fdic = margin_amount_sh if market.lower()=='sh' else margin_amount_sz
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../dates_save', config.get(cfg_sec, 'fpath'))
    up_date = config.get(cfg_sec, 'update_date')
    next_date = config.get(cfg_sec, 'next_update')
    if market.lower()=='sh':
        # 第二个自然日七时
        up_time = pd.to_datetime(next_date)+pd.offsets.Hour(31)
    else:
        # 第二个交易日九时
        up_time = get_delta_trade_day(next_date)+pd.offsets.Hour(9)
    now_time = datetime.datetime.now()
    new_date = get_delta_trade_day(next_date).strftime('%Y-%m-%d')
    if not os.path.exists(fpth):
        config.set(cfg_sec, 'update_date', next_date)
        config.set(cfg_sec, 'next_update', new_date)
        config.write(open(fpth,'w'))
        qvix_pds = mrg_pd_fdic(next_date)
        qvix_pds.to_csv(fpth, mode='w')
    elif now_time < up_time:
        pass
    elif now_time>=up_time:
        # 这里用配置文件中的日期更新数据
        config.set(cfg_sec, 'update_date', next_date)
        config.set(cfg_sec, 'next_update', new_date)
        qvix_pds = mrg_pd_fdic(next_date)
        qvix_pds.to_csv(fpth, mode='a', header=False)
        config.write(open(cfg_file,'w'))

if __name__=='__main__':
    append_margin_file('sh')
    append_margin_file('sz')