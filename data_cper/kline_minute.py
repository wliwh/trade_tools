# 由tdx导出指数的高频数据重新整理
# 或由joinquant获取高频数据

import os
import os.path as osp
import numpy as np
import pandas as pd
import datetime as dt
import efinance as ef
from common.trade_date import get_delta_trade_day

Tdx_Data_Dir = r'C:\\new_tdx_zcgl\\T0002\\export'
All_Name = os.listdir(Tdx_Data_Dir)
All_Pth = [osp.join(Tdx_Data_Dir,p) for p in All_Name]
Save_Csv_Dir = osp.join(osp.dirname(__file__),'..\\kmin')
Saved_Txt_Pth = [osp.join(Save_Csv_Dir,p)for p in os.listdir(Save_Csv_Dir)
                        if p.endswith('txt')]



def get_first_close(name:str,code:str,dts:str)->float:
    ''' 查询开始日期前一日的收盘价 '''
    dt = dts.replace('/','').replace('-','')
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

def get_preday_close(pp:pd.DataFrame, dts:list)->dict:
    ''' 前一日收盘价 '''
    dt2clost = dict()
    for od,d in zip(dts[:-1],dts[1:]):
        dt2clost[d] = pp.loc[pd.to_datetime(od+' 15'),'close']
    return dt2clost

def make_tdx2tab(code:str,name:str,p:str)->pd.DataFrame:
    if code=='999999': code='000001'
    tmp = pd.read_table(p,encoding='gb2312',skiprows=1)
    tmp = tmp.iloc[:-1]
    tmp.columns = ('date','time','open','high','low','close','amount','vol')
    datas = sorted(list(set(tmp['date'])))
    first_d = dt.datetime.strftime(get_delta_trade_day(datas[0],-1),'%Y-%m-%d')
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

def change_jq_file(p:pd.DataFrame,name:str):
    _eob = p['eob']
    eob = _eob.apply(lambda x:pd.to_datetime(x[:-6]))
    tmp = p.drop('eob',axis=1)
    tmp.index = eob
    tmp.index.name = 'date'
    datas = sorted(list(set(x[:10] for x in _eob)))
    first_d = dt.datetime.strftime(get_delta_trade_day(datas[0],-1),'%Y/%m/%d')
    kold_cls = get_preday_close(tmp,datas)
    if name=='上证综指': name='上证指数'
    print(name)
    kold_cls[datas[0]] = get_first_close(name, '', first_d)
    tmp.insert(4,'pdclose',np.nan)
    for d in datas:
        tmp.loc[tmp.index.strftime('%Y-%m-%d')==d,'pdclose'] = kold_cls[d]
    return tmp

def save_tdx_tabs():
    for p in All_Pth:
        with open(p,'r') as f:
            fline = f.readline()
        code,name,freq,fqn = fline.strip().split()
        tb = make_tdx2tab(code,name,p)
        tb.to_csv(osp.join(Save_Csv_Dir,name+'.csv'))

def remove_txt_file():
    for p in Saved_Txt_Pth:
        os.remove(p)

def save_jq_tabs():
    for p in Saved_Txt_Pth:
        nm = osp.basename(p)[:-4]
        csv_nm = p[:-4]+'.csv'
        vp = pd.read_csv(p,index_col=0)
        ncsv = change_jq_file(vp,nm)
        if osp.exists(csv_nm):
            old_p = pd.read_csv(csv_nm,index_col=0)
            old_max_day = old_p.index.max()
            ncsv = ncsv[ncsv.index>old_max_day]
            ncsv = pd.concat([old_p,ncsv],axis=0)
            ncsv.to_csv(csv_nm)
        else:
            ncsv.to_csv(csv_nm)


# save_jq_tabs()