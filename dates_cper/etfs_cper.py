# 引入常用库
import pandas as pd
import numpy as np
import akshare as ak
import efinance as ef
import statsmodels.api as sm
import scipy.stats as st
import datetime as dt
import time
from tqdm import tqdm
import sys
import os
sys.path.append('..')
os.chdir(os.path.dirname(__file__))
from common.smooth_tool import get_near_trade_date

Near_Trade_Date = get_near_trade_date()


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


Funds_Type_Dict = get_funds_dict()


def funds_trade_table(ftype_dict: dict = Funds_Type_Dict) -> pd.DataFrame:
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
                    # TODO: IFNO记录无法查到的基金
                    print('>>>', tp, code)
                bar.update(1)
    return pd.concat(trade_lst, axis=0)


def funds_trade_csv() -> pd.DataFrame:
    ''' 读取场内基金每日交易信息 '''
    csv_path = 'funds_amt_'+Near_Trade_Date+'.csv'
    for c in os.listdir('./'):
        if c.endswith('csv') and c!=csv_path:
            os.remove(c)
    if not os.path.exists(csv_path):
        funds_trade = funds_trade_table()
        funds_trade.to_csv(csv_path)
        return funds_trade
    else:
        return pd.read_csv(csv_path)


Funds_Trade = funds_trade_csv()


def funds_amt_rate_table(rate: bool, 
                         f_trade: pd.DataFrame = Funds_Trade,
                         f_type_dict: dict = Funds_Type_Dict) -> pd.DataFrame:
    ''' 场内基金按照类别计算的每日成交额 '''
    funds_type_amt = [f_trade[f_trade['类型'] == k].groupby(
        '日期').agg({'成交额': 'sum'}) for k in f_type_dict.keys()]
    funds_type_amt = pd.concat(funds_type_amt, axis=1)
    funds_type_amt.columns = f_type_dict.keys()
    funds_type_amt['sum'] = funds_type_amt.sum(axis=1)
    funds_type_amt /= 1e8
    funds_type_per = funds_type_amt.copy()
    _funds_sum = funds_type_per.pop('sum')
    funds_type_per = funds_type_per.div(_funds_sum, axis=0)
    return funds_type_per if rate else funds_type_amt