import pandas as pd
import numpy as np
import akshare as ak
import os,sys

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

def get_funds_rate(windows=150)->pd.DataFrame:
    ''' 公募基金仓位高低分位 '''
    funds_pos = get_funds_postions()
    return min_max_dist_pd(funds_pos,windows=windows)


def get_hsgt_acc_flow():
    ''' 获取北向资金累计买入额 '''
    north_acc_flow = ak.stock_hsgt_north_acc_flow_in_em('北上')
    north_acc_flow.set_index('date',inplace=True)
    north_acc_flow/=1e4
    sh_acc_flow = ak.stock_hsgt_hist_em('沪股通')
    sz_acc_flow = ak.stock_hsgt_hist_em('深股通')
    # TODO: index 格式需要调整
    north_pad_flow = sh_acc_flow['历史累计净买额'].add(sz_acc_flow['历史累计净买额'],fill_value=0)
    # north_acc_flow['acc_pay'] = 
    return north_acc_flow

print(get_hsgt_acc_flow())