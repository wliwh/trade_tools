import configparser
import os
import sys
import time
import pandas as pd
import numpy as np
import akshare as ak
import datetime

NowDate = datetime.date.today().strftime('%Y-%m-%d')

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
    pass