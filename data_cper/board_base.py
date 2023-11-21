import configparser
import os
import sys
import time
import pandas as pd
import numpy as np
import akshare as ak
import datetime
from common.trade_date import get_delta_trade_day

NowDate = datetime.date.today().strftime('%Y-%m-%d')
BSCode = {'上证50':'000016','沪深300':'000300',
          '中证500':'000905','中证1000':'000852',
          '国证2000':'399303','中证2000':'932000',
          '国证A指':'399317'}


def bs_index_row(code,start,end):
    s = start.replace('-','')
    e = end.replace('-','')
    if s<'20230814' and code==BSCode['中证2000']:
        return None
    tmp = ak.index_zh_a_hist(code,start_date=s,end_date=e)
    tmp.columns = ['date','open','close','high','low','vol','amt','hlpct','pct','inc','hs']
    tmp['oclose'] = tmp['close'].shift(1)
    tmp['volpct'] = tmp['vol']/(tmp['vol'].shift(1))*100-100
    tmp['code'] = code
    tmp['opct'] = tmp['open']/tmp['oclose']*100.0-100.0
    tmp['dpct'] = tmp['close']/tmp['open']*100.0-100.0
    tmp['stzb'] = abs(tmp['open']-tmp['close'])/(tmp['high']-min(tmp['open'],tmp['close']))
    tmp = tmp.loc[1,['date','code','volpct','pct','opct','dpct','stzb']]
    return tmp

def get_bs_price(date):
    ''' 获取大小盘在某日的涨跌幅 '''
    pre_day = get_delta_trade_day(date,-1).strftime('%Y%m%d')
    bs_tb = list()
    for _, code in BSCode.items():
        brow = bs_index_row(code,pre_day,date)
        if brow:
            bs_tb.append(brow)
    return pd.DataFrame(bs_tb)

def get_bs_price_min(date,min_tm=30):
    pass

def get_board_codes(spt:str='sw') -> pd.Series:
    if spt=='sw':
        return ak.sw_index_first_info()['行业代码']
    elif spt=='ths':
        return ak.stock_board_industry_summary_ths()['板块']
    elif spt=='em':
        return ak.stock_board_industry_name_em()['板块名称']
    

def get_board_price(codes:pd.Series,
                    spt:str='sw',
                    start_date:str='20180101') -> pd.DataFrame:
    name_lst, price_series = list(),list()
    for c in codes:
        name_lst.append(c)
        if spt=='sw':
            _tmp = ak.index_hist_sw(symbol=c[:6], period="day")
            _tmp = _tmp[_tmp['日期']>=pd.Timestamp(start_date)]
        elif spt=='ths':
            _tmp = ak.stock_board_industry_index_ths(c,start_date=start_date,end_date=NowDate)
            _tmp.rename(columns=lambda x:x.replace('价',''),inplace=True)
        elif spt=='em':
            time.sleep(0.3)
            _tmp = ak.stock_board_industry_hist_em(c,start_date=start_date,end_date=NowDate)
        _df = _tmp[['日期','收盘']]
        _df.set_index('日期',inplace=True)
        _df.rename(columns={'收盘':'收盘_'+c},inplace=True)
        price_series.append(_df)
    board_close =  pd.concat(price_series,axis=1)
    return board_close.dropna()


def calc_board_pct_sort(board_price:pd.DataFrame,
                        windows:int=5,
                        sortit:bool=False):
    board_pct = board_price.pct_change(windows).dropna()*100
    if sortit:
        board_st = board_pct.rank(axis=1,method='min',ascending=False)
        return board_st
    return board_pct

def calc_board_cycle_position(board_st:pd.DataFrame):
    ''' 计算板块轮动强度 '''
    return board_st.diff().abs().sum(axis=1)


def calc_board_cycle_ginni(board_st:pd.DataFrame):
    ''' 计算板块间基尼系数 '''
    lens,_ = board_st.shape
    board_ginni = pd.Series(0,index=board_st.index)
    for i in range(lens):
        s0 = board_st.iloc[i]
        se = s0.sort_values()
        se = (se-se[0])/(se[-1]-se[0])
        g1 = se.sum()/len(se)
        g2 = (se[0]+se[-1])/2
        board_ginni.iloc[i] = g1/g2
    return board_ginni

