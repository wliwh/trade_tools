# 引入常用库
import configparser
import datetime
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import akshare as ak
import efinance as ef
import time
from tqdm import tqdm
import sys
import os
sys.path.append('..')
os.chdir(os.path.dirname(__file__))
from common.trade_date import get_trade_day, get_delta_trade_day, get_next_weekday
from common.mpf_set import M80_20
from .md_temp import ETF_Amount_Texts

Funds_Type_Dic = dict(gp='股票',zq='债券',qdii='跨境',
                      sp='商品',hb='货币',kzz='可转债')

def get_funds_dict() -> dict:
    ''' 获取场内交易基金代码, 按类型分类：
            gp: 股票类指数
            zq: 债券, 长债或中短债
            kzz: 可转债
            hb: 场内货币
            qdii: 场内QDII, 跨境
            sp: 商品, 黄金
    '''
    bfunds = ak.fund_etf_spot_em()
    # ETF 基金实时行情. 比后两者多场内货币基金以及部分停牌的股票基金，缺少部分债权类、商品类基金
    funds = ak.fund_etf_fund_daily_em()
    # funds = ak.fund_em_exchange_rank()
    # 场内基金净值、排行情况. 两者获取的场内基金列表一致
    #  em_exchange_rank 没有类型这一属性
    explict_code = set(bfunds['代码']) - set(funds['基金代码'])
    tp_code = [e for e in explict_code if e >= '512000']
    # TODO: 获取停牌的场内基金（除货币外均为股票基金）代码，过滤方法需调整
    if '成立日期' in funds.columns:
        funds.sort_values('成立日期', inplace=True)
        funds.index = range(len(funds))
    funds.loc[funds['基金代码'] == '159834', '类型'] = '商品（不含QDII）'
    # 修改 159834-南方上海金ETF 的类型错误
    funds_type_dict = {
        'gp': funds[funds['类型'] == '指数型-股票']['基金代码'].to_list() + tp_code,
        'zq': funds[(funds['类型'] == '债券型-长债') | (funds['类型'] == '债券型-中短债')]['基金代码'].to_list(),
        'kzz': funds[funds['类型'] == '债券型-可转债']['基金代码'].to_list(),
        'hb': [e for e in explict_code if e < '512000'],
        'qdii': funds[funds['类型'] == 'QDII']['基金代码'].to_list(),
        'sp': funds[funds['类型'] == '商品（不含QDII）']['基金代码'].to_list()}
    return funds_type_dict


def funds_realtime_info(ftype_dict: dict) -> pd.DataFrame:
    ''' 快速更新当日etf信息, 调整表格形态[会缺失部分etf信息] '''
    # etf_lsts 属于 funds
    funds2type = {c: k for k, v in ftype_dict.items() for c in v}
    etf_lsts = ef.stock.get_realtime_quotes(['ETF'])
    etf_lsts.rename(
        columns={'最新交易日': '日期', '今开': '开盘', '最新价': '收盘'}, inplace=True)
    etf_lsts['换手率'].replace('-', 0, inplace=True)
    etf_lsts = etf_lsts[etf_lsts['开盘'] != '-']
    etf_lsts.astype({'开盘': 'float64', '收盘': 'float64', '最高': 'float64', '最低': 'float64',
                    '成交量': 'int64', '成交额': 'float64', '涨跌幅': 'float64', '涨跌额': 'float64', '换手率': 'float64'})
    etf_lsts['振幅'] = (etf_lsts['最高']-etf_lsts['最低'])/etf_lsts['最高']
    etf_lsts = etf_lsts[['股票名称', '股票代码', '日期', '开盘', '收盘',
                         '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅', '涨跌额', '换手率']]
    etf_lsts['类型'] = [funds2type[k] for k in etf_lsts['股票代码']]
    return etf_lsts


def funds_divide_dict(etf_pd: pd.DataFrame, ftype_dict: dict) -> dict:
    ''' 找出快速更新etf中缺失的代码. 按类型分组 '''
    etf_names_set = set(etf_pd['股票代码'])
    etf_explict_dict = dict()
    for k in ftype_dict.keys():
        etf_explict_dict[k] = list(set(ftype_dict[k])-etf_names_set)
    return etf_explict_dict


def funds_quote_table(ftype_dict: dict) -> pd.DataFrame:
    ''' 快速更新缺失etf的最后一日信息 '''
    explict_pd_lst = list()
    for tp, lst in ftype_dict.items():
        dfm = pd.DataFrame([e.iloc[-1] for e in ef.stock.get_quote_history(lst).values() if not e.empty])
        dfm['类型'] = tp
        explict_pd_lst.append(dfm)
    explict_pd =  pd.concat(explict_pd_lst, axis=0)
    return explict_pd


def funds_trade_table(ftype_dict: dict) -> pd.DataFrame:
    ''' 合并所有场内基金的日频交易信息 '''
    trade_lst = list()
    alens = sum(map(len, ftype_dict.values()))
    with tqdm(total=alens) as bar:
        for tp, clst in ftype_dict.items():
            for code in clst:
                time.sleep(0.5)
                try:
                    pd1 = ef.stock.get_quote_history(code)
                    pd1['类型'] = tp
                    trade_lst.append(pd1)
                except KeyError as e:
                    # TODO: IFNO 记录无法查到的基金
                    print('>>>', tp, code)
                bar.update(1)
    return pd.concat(trade_lst, axis=0)


def append_funds_trade_file(cfg_file='') -> pd.DataFrame:
    ''' 更新场内基金每日交易信息 '''
    ftype_dict = get_funds_dict()
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec, cfg_wsec = 'Etf_Amount', 'Etf_Amount_All'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get(cfg_sec, 'fpath'))
    up_date = config.get(cfg_sec, 'update_date')
    next_date = config.get(cfg_sec, 'next_update')
    # up_week = config.get(cfg_wsec,'update_date')s
    next_week = config.get(cfg_wsec,'next_update')
    now_date = get_trade_day(17).strftime('%Y-%m-%d')
    today_date = datetime.date.today().strftime('%Y-%m-%d')
    next_day = get_delta_trade_day(now_date).strftime('%Y-%m-%d')
    # get_next_weekday(next_week,6)
    if not os.path.exists(fpth):
        funds_trade = funds_trade_table(ftype_dict)
        funds_trade.to_csv(fpth,mode='w')
        config.set(cfg_sec, 'update_date', now_date)
        config.set(cfg_sec, 'next_update', next_day)
        config.write(open(cfg_file,'w'))
        return 'week', now_date
    elif next_date<=now_date:
        # 交易日更新
        old_trade_pd = pd.read_csv(fpth,index_col=0)
        os.remove(fpth)
        realtime_pd = funds_realtime_info(ftype_dict)
        explict_name = funds_divide_dict(realtime_pd, ftype_dict)
        explict_pd = funds_quote_table(explict_name)
        explict_pd = explict_pd[explict_pd['日期']==now_date]
        new_trade_pd = pd.concat(
            [old_trade_pd, realtime_pd, explict_pd], axis=0)
        new_trade_pd.drop_duplicates(inplace=True)
        new_trade_pd.to_csv(fpth, mode='w')
        config.set(cfg_sec, 'update_date', now_date)
        config.set(cfg_sec, 'next_update', next_day)
        config.write(open(cfg_file,'w'))
        return 'day', now_date
    elif next_week<=today_date:
        # 周级别更新
        os.remove(fpth)
        funds_trade = funds_trade_table(ftype_dict)
        funds_trade.to_csv(fpth, mode='w')
        config.set(cfg_wsec, 'update_date', now_date)
        config.set(cfg_wsec, 'next_update', get_next_weekday(now_date,6).strftime('%Y-%m-%d'))
        config.write(open(cfg_file,'w'))
        return 'week', now_date
    elif (up_date==now_date) or (next_week>now_date):
        return 0, 0
    return 0, 0


def funds_amt_rate_table(rate: bool, f_trade: pd.DataFrame, f_type_dict: dict) -> pd.DataFrame:
    ''' 场内基金按照类别计算的每日成交额 '''
    funds_type_amt = [f_trade[f_trade['类型'] == k].groupby(
        '日期').agg({'成交额': 'sum'}) for k in f_type_dict.keys()]
    funds_type_amt = pd.concat(funds_type_amt, axis=1)
    funds_type_amt.columns = f_type_dict.keys()
    funds_type_amt['sum'] = funds_type_amt.sum(axis=1)
    funds_type_amt /= 1e8
    funds_type_amt.index.name = 'date'
    funds_type_per = funds_type_amt.copy()
    _funds_sum = funds_type_per.pop('sum')
    funds_type_per = funds_type_per.div(_funds_sum, axis=0)
    return funds_type_per if rate else funds_type_amt

def funds_amt_pct(winds:list, ftype_dict:dict, famt_per:pd.DataFrame)->pd.DataFrame:
    ''' 场内基金按类别计的成交额分位数
        读取每日 etf_amount 详细数据 '''
    famt_per.sort_index(inplace=True)
    famt_per = famt_per.tail(2000)*100
    wind_l = list(sorted(winds,reverse=True))
    famt_hls = pd.DataFrame(
        np.zeros((len(famt_per),len(winds)*len(ftype_dict))),
        index=famt_per.index,
        columns=['%s_%d' % (n,w) 
                 for w in wind_l for n in ftype_dict.keys()])
    ftp1,*_, ftp2 = ftype_dict.keys()
    famt_hls.loc[:,:] = np.nan
    for w in wind_l:
        for i in range(w,len(famt_per)+1):
            famt_hls.iloc[i-1][ftp1+'_'+str(w):ftp2+'_'+str(w)] = (famt_per.iloc[i-w:i]<=famt_per.iloc[i-1]).sum()/w
    return famt_hls

def funds_amt_words_lst(winds:tuple, ftype_lst, famt_per:dict, famt_q:dict)->str:
    ''' 输出成交额比值和相应的分位数 '''
    wind_l = list(sorted(winds,reverse=False))
    famt_lst = list()
    basic_lines = '1. {}({}):\t{:.2f}\t{}, {}, {}'
    for ft_nm in ftype_lst:
        b_qs = [M80_20(famt_q[ft_nm+'_'+str(w)]) for w in wind_l]
        b_l = basic_lines.format(
            Funds_Type_Dic[ft_nm],
            ft_nm,
            famt_per[ft_nm],
            *b_qs)
        famt_lst.append(b_l)
    return '\n'.join(famt_lst)

def docs_funds_amt(cfg_file=''):
    ''' 填写场内基金信息 '''
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec = 'Etf_Amount'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get(cfg_sec, 'fpath'))
    img_pth = os.path.join('../data_save', config.get('Basic_Info','doc_img_pth'),'etf_amount_per.png')
    up_date = config.get(cfg_sec, 'update_date')
    all_periods = config.get(cfg_sec, 'etf_amount_periods')
    all_prds = [int(a.strip()) for a in all_periods.split(',')]
    etf_table = pd.read_csv(fpth,index_col=0)
    famt_dic = {s:0 for s in set(etf_table['类型'])}

    etf_per = funds_amt_rate_table(True,etf_table,famt_dic)
    etf_qut = funds_amt_pct(all_prds,famt_dic,etf_per)
    etf_words_lst = funds_amt_words_lst(all_prds,Funds_Type_Dic.keys(),dict(etf_per.loc[up_date]*100.0),dict(etf_qut.loc[up_date]*100.0))
    etf_amt_pics = etf_per.tail(210).plot(x_compat=True)
    etf_amt_ppth = plt.savefig(img_pth,dpi=400,bbox_inches='tight')
    etf_amt_text_dic = dict(
        etf_amount_periods=all_periods,
        etf_amount_tlst=etf_words_lst,
        etf_amount_plt_pth=img_pth
    )
    # print(etf_amt_text_dic)
    return etf_amt_text_dic


if __name__=='__main__':
    # append_funds_trade_file()
    print(ETF_Amount_Texts.format(**docs_funds_amt()))
    pass