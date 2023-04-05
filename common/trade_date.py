import pandas as pd
import akshare as ak
import datetime

Trade_List = ak.tool_trade_date_hist_sina()

def get_near_trade_date(new_hour=16)->str:
    ''' 获取最近的交易日, new_hour 为判断新交易日的分割小时 '''
    sh_trade_date_list = ak.tool_trade_date_hist_sina()
    today_time = datetime.datetime.now()
    near_trade_date = sh_trade_date_list[sh_trade_date_list<=today_time.date()].dropna().iloc[-1 if (today_time.hour>=new_hour) else -2,0]
    near_trade_date = near_trade_date.strftime('%Y-%m-%d')
    return near_trade_date

def get_trade_day(cut_hour=16):
    ntime = datetime.datetime.now()
    n_idx = (Trade_List.trade_date<=ntime.date()).argmin()
    return Trade_List.loc[n_idx-1 if ntime.hour>=cut_hour else n_idx-2,'trade_date']

def get_delta_trade_day(day:str,delta:int=1):
    ndate = datetime.datetime.strptime(day,"%Y-%m-%d").date()
    n_idx = (Trade_List.trade_date>ndate).argmax()
    if delta>0: 
        return Trade_List.loc[n_idx+delta-1,'trade_date']
    n_trade = day if ndate in Trade_List.trade_date.values else None
    if delta==0: 
        return n_trade if n_trade else None
    else: 
        return Trade_List.loc[n_idx+delta-(1 if n_trade else 0),'trade_date']

def get_next_weekday(day:str,weekday=6):
    nday = get_delta_trade_day(day,1)
    return nday+pd.offsets.Week(1,weekday=weekday-1)
