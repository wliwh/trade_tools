# 由tdx导出指数的高频数据重新整理

import os
import os.path as osp
import numpy as np
import pandas as pd
from common.trade_date import get_delta_trade_day
import datetime as dt
import efinance as ef

tdx_data_dir = r'C:\\new_tdx_zcgl\\T0002\\export'
save_csv_dir = osp.join(osp.dirname(__file__),'..\\kmin')
all_name = os.listdir(tdx_data_dir)
all_pth = [osp.join(tdx_data_dir,p) for p in all_name]


def get_first_close(name:str,code:str,dts:str)->float:
    ''' 查询开始日期前一日的收盘价 '''
    dt = dts.replace('/','')
    tt = ef.stock.get_quote_history(name,beg=dt,end=dt,fqt=0)
    if tt.empty:
        tt = ef.stock.get_quote_history(code,beg=dt,end=dt,fqt=0)
    return tt['收盘'][0]

def get_next_close(pp:pd.DataFrame,dts:list)->dict:
    ''' 查询前一日的收盘价 '''
    dt2clost = dict()
    for od,d in zip(dts[:-1],dts[1:]):
        dt2clost[d] = pp.loc[(pp['date']==od) & (pp['time']==1500.0),'close'].values[0]
    return dt2clost

def make_tdx2tab(code:str,name:str,p:str)->pd.DataFrame:
    if code=='999999': code='000001'
    tmp = pd.read_table(p,encoding='gb2312',skiprows=1)
    tmp = tmp.iloc[:-1]
    tmp.columns = ('date','time','open','high','low','close','amount','vol')
    datas = sorted(list(set(tmp['date'])))
    first_d = dt.datetime.strftime(get_delta_trade_day(datas[0],-1),'%Y/%m/%d')
    kold_cls = get_next_close(tmp,datas)
    print(code,name)
    kold_cls[datas[0]] = get_first_close(name, code, first_d)
    tmp.insert(6,'pdclose',np.nan)
    for d in datas: tmp.loc[tmp['date']==d,'pdclose'] = kold_cls[d]
    dtime = [pd.to_datetime('{} {:04d}'.format(d,int(t))) for d,t in tmp[['date','time']].values]
    tmp.index = dtime
    tmp.index.name = 'date'
    tmp = tmp.loc[:,'open':'vol']
    return tmp

def save_tabs():
    for p in all_pth:
        with open(p,'r') as f:
            fline = f.readline()
        code,name,freq,fqn = fline.strip().split()
        tb = make_tdx2tab(code,name,p)
        tb.to_csv(osp.join(save_csv_dir,name+'.csv'))


# print(make_tdx2tab(all_pth[0]))
save_tabs()