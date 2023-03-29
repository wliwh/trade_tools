import pandas as pd
import numpy as np
import akshare as ak
import os,sys
import talib

sys.path.append('..')
os.chdir(os.path.dirname(__file__))
from common.smooth_tool import min_max_dist_pd


def get_funds_postions()->pd.DataFrame:
    ''' 获取公募基金[股票型、混合平衡型、灵活配置型]仓位，每周更新 '''
    gp_pos = ak.fund_stock_position_lg()
    bal_pos = ak.fund_balance_position_lg()
    smt_pos = ak.fund_linghuo_position_lg()
    funds_pos = pd.DataFrame({'gp':gp_pos['position'].values,
                              'bal':bal_pos['position'].values,
                              'smt':smt_pos['position'].values},
                              index=gp_pos['date'])
    return funds_pos

def get_funds_rate(funds_pos:pd.DataFrame, windows=150)->pd.DataFrame:
    ''' 公募基金仓位高低分位 (长期-150周) '''
    return min_max_dist_pd(funds_pos, windows=windows)


def get_hsgt_acc_flow():
    ''' 北向累计净流入、累计净买入资金量 '''
    north_acc_flow = ak.stock_hsgt_north_acc_flow_in_em('北上')
    north_acc_flow.set_index('date',inplace=True)
    north_acc_flow/=1e4
    sh_acc_flow = ak.stock_hsgt_hist_em('沪股通').set_index('日期')
    sz_acc_flow = ak.stock_hsgt_hist_em('深股通').set_index('日期')
    # TODO: 2020-10-13 数据空缺
    north_pad_flow = sh_acc_flow['历史累计净买额'].add(sz_acc_flow['历史累计净买额'],fill_value=0)
    north_pad_flow.index = [d.strftime('%Y-%m-%d') for d in north_pad_flow.index]
    north_pad_flow.index.name = 'date'
    north_acc_flow.columns = ['inflow']
    north_acc_flow['purchase'] = north_pad_flow
    north_acc_flow.fillna(method='ffill',inplace=True)
    return north_acc_flow

def get_north_flow_bias(north_flow:pd.DataFrame, N=20,window=120,ma_type='ma'):
    ''' 北向流入资金偏离度及其分位数 '''
    north_name = north_flow.columns
    ma_fun_dic = {'ma':talib.MA,'ema':talib.EMA}
    ma_fun = ma_fun_dic.get(ma_type,talib.MA)
    for i in range(north_flow.shape[1]):
        north_flow[north_name[i]+'_bias'] = north_flow.iloc[:,i]/ma_fun(north_flow.iloc[:,i],N)*100-100
        north_flow[north_name[i]+'_brate'] = min_max_dist_pd(north_flow,window,north_name[i]+'_bias')
    return north_flow
