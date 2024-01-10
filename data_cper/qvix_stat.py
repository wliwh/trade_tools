import pandas as pd
import numpy as np
import re
import os
import sys
import akshare as ak
import configparser
import matplotlib.pyplot as plt
import mplfinance as mpf
import talib
# sys.path.append('..')
os.chdir(os.path.dirname(__file__))

from common.trade_date import get_trade_day, get_delta_trade_day, get_trade_day_between
from common.mpf_set import Mpf_Style,M80_20
from common.smooth_tool import LLT_MA, HMA, super_smoother, min_max_dist_series


def parse_symbol_str(symbol: str, minute: bool = False):
    ''' symbol 输出 '''
    rcp = re.compile(r'(index|cyb)?(1000|500|300|50)?(etf)?', re.IGNORECASE)
    c_pre, c_mid, _ = rcp.match(symbol).groups()
    if c_pre and c_pre.lower() == 'index' and c_mid == '1000':
        return 'index1000' if minute else 'Index1000'
    elif c_pre and symbol.lower() == 'cyb':
        return 'cyb' if minute else 'CYB'
    elif not c_pre and c_mid:
        if symbol.lower() in ('1000', '1000etf'):
            return 'index1000' if minute else 'Index1000'
        elif symbol[len(c_mid):].lower() in ('', 'etf'):
            return c_mid if minute else c_mid+'ETF'
    else:
        return None


def _test_parse():
    symbol_lst = [
        'index1000', 'Index1000', 'index', 'index10',
        'cyb', 'CYB', 'Cyb', 'cyb300', 'cyb12', '300cyb',
        '50', '300', '500', '1000', '200', '1000etf',
        '50Etf', 'cc300ETF', 'indexETF', '50k'
    ]
    for s in symbol_lst:
        print(s, parse_symbol_str(s))


def option_qvix(symbol: str = '50ETF') -> pd.DataFrame:
    """
    期权波动率指数 QVIX
    http://1.optbbs.com/s/vix.shtml?{symbol}
    [可选: 50ETF, 300ETF, 500ETF, CYB, Index1000]
    :return: 期权波动率指数 QVIX
    :rtype: pandas.DataFrame
    """
    symbol = parse_symbol_str(symbol, False)
    url = "http://1.optbbs.com/d/csv/d/k.csv"
    index_col_dict = {
        '50ETF': [0, 1, 2, 3, 4],
        '300ETF': [0, 9, 10, 11, 12],
        '500ETF': [0, 67, 68, 69, 70],
        'CYB': [0, 71, 72, 73, 74],
        'Index1000': [0, 25, 26, 27, 28]
    }
    temp_df = pd.read_csv(url).iloc[:, index_col_dict[symbol]]
    temp_df.columns = [
        "date",
        "open",
        "high",
        "low",
        "close",
    ]
    temp_df["date"] = pd.to_datetime(temp_df["date"]).dt.date
    temp_df.dropna(inplace=True)
    return temp_df


def option_min_qvix(symbol='50') -> pd.DataFrame:
    """
    期权波动率指数 QVIX - 分钟级
    http://1.optbbs.com/s/vix.shtml?{symbol}
    [可选: 50,300,500,cyb,index1000]
    :return: 期权波动率指数 QVIX
    :rtype: pandas.DataFrame
    """
    symbol = parse_symbol_str(symbol, True)
    url = f"http://1.optbbs.com/d/csv/d/vix{symbol}.csv"
    temp_df = pd.read_csv(url)
    if temp_df.shape[1]>1:
        pass
    elif temp_df.shape[1]==1:
        vls = [p[0].split('\t') for p in temp_df.values]
        temp_df = pd.DataFrame(vls,columns=temp_df.columns[0].split('\t'))
    temp_df = temp_df.iloc[:, :2]
    temp_df.columns = [
        "time",
        "qvix",
    ]
    return temp_df

def _option_call_put_positon(p1:pd.DataFrame,ename:str='510050'):
    tt = p1.copy()
    s1,s2,s3,s4 = [],[],[],[]
    # tt[['call_pos','call5','put_pos','put5']] = np.nan
    for t in tt.date:
        s_t = t.strftime('%Y%m%d')
        try:
            rr=ak.option_lhb_em(ename,'期权持仓情况-认购持仓量',s_t)
            amts=rr.loc[rr['机构']=='总成交量','持仓量'].values[0]
            amt5=rr.loc[rr['机构']=='前五名合计','持仓量'].values[0]
            s1.append(amts); s2.append(amt5)
        except:
            s1.append(np.nan); s2.append(np.nan)
            print('call',s_t)
        try:
            r2=ak.option_lhb_em(ename,'期权持仓情况-认沽持仓量',s_t)
            amps=rr.loc[r2['机构']=='总成交量','持仓量'].values[0]
            amp5=rr.loc[r2['机构']=='前五名合计','持仓量'].values[0]
            s3.append(amps); s4.append(amp5)
        except:
            s3.append(np.nan); s4.append(np.nan)
            print('put', s_t)
    tt['call_pos'] = s1; tt['call5'] = s2
    tt['put_pos'] = s3; tt['put5'] = s4
    return tt

def _make_option_day_pds():
    symb_lst = ('50ETF','300ETF','500ETF','CYB','1000ETF')
    ss_pds = list()
    for s in symb_lst:
        print('>>>', s)
        p1 = option_qvix(s)
        p1.insert(1,'code',s)
        if s in ('50ETF','300ETF'):
            p1 = _option_call_put_positon(p1,'510050' if s=='50ETF' else '510300')
        ss_pds.append(p1)
    ss_tb = pd.concat(ss_pds,axis=0)
    ss_tb.set_index('date',inplace=True)
    ss_tb.sort_index(inplace=True)
    ss_tb.to_csv('qvix_day.csv')
    # return ss_tb

def update_qvix_infos(dt_lst:list) -> pd.DataFrame:
    ''' 根据时间列表填充qvix数据 '''
    symb_lst = ('50ETF','300ETF','500ETF','CYB','1000ETF')
    ss_pds = list()
    for s in symb_lst:
        p1 = option_qvix(s)
        p1 = p1[p1['date'].apply(lambda x:x in dt_lst)]
        p1.insert(1,'code',s)
        if s in ('50ETF','300ETF'):
            p1 = _option_call_put_positon(p1,'510050' if s=='50ETF' else '510300')
        ss_pds.append(p1)
    ss_tb = pd.concat(ss_pds,axis=0)
    ss_tb.set_index('date',inplace=True)
    ss_tb.sort_index(inplace=True)
    return ss_tb

# print(type(update_qvix_infos([pd.to_datetime('2024-01-08').date()]).index[-1]))

def qvix_minute_pds(pref_date=''):
    ''' QVIX 分钟级数据汇总 '''
    qvix_min_pd = pd.DataFrame()
    sym_lsts = ('300ETF', '500ETF', 'CYB', '1000ETF')
    qvix_50 = option_min_qvix('50')
    qvix_min_pd.index = pd.to_datetime(pref_date + ' ' + qvix_50['time'])
    qvix_min_pd['50ETF'] = qvix_50['qvix'].values
    for sym in sym_lsts:
        qvix_min_pd[sym] = option_min_qvix(sym)['qvix'].values
    return qvix_min_pd


def append_qvix_day_file(cfg_file=''):
    ''' 更新qvix日级别数据 '''
    if not cfg_file:
        cfg_file = '../trade.ini'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get('Qvix_Day', 'fpath'))
    up_date = config.get('Qvix_Day', 'update_date')
    next_date = config.get('Qvix_Day', 'next_update')
    now_date = get_trade_day(16).strftime('%Y-%m-%d')
    next_day = get_delta_trade_day(now_date).strftime('%Y-%m-%d')
    # print(up_date, now_date, next_date)
    if up_date>=now_date:
        return 0
    elif next_date <= now_date:
        dlst = get_trade_day_between(up_date,16,False)
        if dlst is None: return 0
        qvix_pds = update_qvix_infos(dlst)
        if qvix_pds.empty: return 0
        m_date = qvix_pds.index[-1].strftime('%Y-%m-%d')
        config.set('Qvix_Day', 'update_date', m_date)
        config.set('Qvix_Day', 'next_update', next_day)
        qvix_pds.to_csv(fpth, mode='a', header=False)
        config.write(open(cfg_file,'w'))
        return now_date
    return 0

def append_qvix_minute_file(cfg_file=''):
    ''' 更新qvix分钟级别数据 '''
    if not cfg_file:
        cfg_file = '../trade.ini'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get('Qvix_Minute', 'fpath'))
    up_date = config.get('Qvix_Minute', 'update_date')
    next_date = config.get('Qvix_Minute', 'next_update')
    now_date = get_trade_day(16).strftime('%Y-%m-%d')
    next_day = get_delta_trade_day(now_date).strftime('%Y-%m-%d')
    if not os.path.exists(fpth):
        print('qvix no.')
        config.set('Qvix_Minute', 'update_date', now_date)
        config.set('Qvix_Minute', 'next_update', next_day)
        config.write(open(fpth,'w'))
        qvix_pds = qvix_minute_pds(now_date)
        qvix_pds.to_csv(fpth, mode='w')
        return now_date
    elif up_date == now_date:
        return 0
    elif next_date <= now_date:
        config.set('Qvix_Minute', 'update_date', now_date)
        config.set('Qvix_Minute', 'next_update', next_day)
        qvix_pds = qvix_minute_pds(now_date)
        qvix_pds.to_csv(fpth, mode='a', header=False)
        config.write(open(cfg_file,'w'))
        return now_date
    return 0

def make_qvix_macd_smooth(symbol='300ETF',smooth='LLT',main_w=120,winds=(20,60,120)):
    ''' qvix日频平滑处理,MACD,ATR 等指标 '''
    otb = option_qvix(symbol)
    otb.set_index('date',inplace=True)
    otb.index = pd.to_datetime(otb.index)
    # 1. macd
    wma1 = otb.close.ewm(span=11,adjust=False).mean()
    wma2 = otb.close.ewm(span=22,adjust=False).mean()
    otb['MACD'] = wma1 - wma2
    otb['Diff'] = otb.MACD.ewm(span=8,adjust=False).mean()
    otb['Hist'] = otb.MACD - otb.Diff
    otb['HistH'] = otb['Hist']
    otb['HistL'] = otb['Hist']
    otb.loc[otb.HistH<0,'HistH'] = np.nan
    otb.loc[otb.HistL>0,'HistL'] = np.nan
    # 2. smooth
    if smooth.upper()=='HMA':
        otb['Smooth'] = HMA(0.5*otb['open']+0.5*otb['close'],11)
    elif smooth.lower()=='smooth':
        otb['Smooth'] = super_smoother(0.5*otb['open']+0.5*otb['close'],11)
    else:
        otb['Smooth'] = LLT_MA(0.5*otb['open']+0.5*otb['close'],1/6)
    otb['Dsmooth'] = 0 - otb['Smooth'] +  otb['close']
    # 0.5*otb['open']+0.5*otb['close']
    otb['Qsmooth'] = min_max_dist_series(otb.Dsmooth,main_w)
    for w in winds: otb['Q_'+str(w)] = min_max_dist_series(otb.Dsmooth,w)
    # 3. ATR
    otb['ATR'] = talib.ATR(otb.high,otb.low,otb.close,11)
    otb['ATRdf'] = otb.ATR.diff()
    return otb

def make_qvix_day_tline(sym,winds,otb_dic:dict):
    ''' 生成某个指数sym相应的QVIX指标及其分位数 '''
    basic_lines = '1. {}:\t{:.2f}\t({},{},{})'
    b_qs = [M80_20(otb_dic['Q_'+str(w)]) for w in winds]
    b_l = basic_lines.format(sym,otb_dic['close'],*b_qs)
    return b_l

def make_qvix_day_plt(otb:pd.DataFrame,fig_pth:str,sym='300ETF',smooth='LLT',smooth_wind=120):
    ''' qvix 绘图 '''
    otb_near = otb.tail(75)
    xadd_plots = [
        mpf.make_addplot(otb_near.Smooth,color='slateblue',ylabel=smooth),
        mpf.make_addplot(otb_near.Dsmooth,type='bar',panel=1,width=0.7, color='lightgray',secondary_y=False,ylabel='DSmooth({})'.format(smooth_wind)),
        mpf.make_addplot(otb_near.Qsmooth,panel=1,color='darkblue',secondary_y=True),
        mpf.make_addplot(otb_near.HistH,type='bar', width=0.7, panel=2, color='red',alpha=0.7,secondary_y=False,ylabel='MACD'),
        mpf.make_addplot(otb_near.HistL,type='bar', width=0.7, panel=2, color='green',alpha=0.7,secondary_y=False,ylabel='MACD'),
        mpf.make_addplot(otb_near.MACD,panel=2,color='gold',secondary_y=True),
        mpf.make_addplot(otb_near.Diff,panel=2,color='deepskyblue',secondary_y=True),
        mpf.make_addplot(otb_near.ATRdf,panel=3,type='bar', width=0.7, ylabel='ATR', color='lightgray',secondary_y=False),
        mpf.make_addplot(otb_near.ATR,panel=3,color='peru',secondary_y=True)
        ]
    mpf.plot(otb_near,type='candle',ylabel='value',
             style=Mpf_Style, addplot=xadd_plots,
             datetime_format='%m-%d',xrotation=15,
             savefig={'fname':fig_pth,'dpi':400,'bbox_inches':'tight'},
             figratio=(6,6),figscale=1.5) # title='\n'+sym+' QVIX'
    
def doc_qvix_day(cfg_file=''):
    ''' 填写 QVIX 信息 '''
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec = 'Qvix_Day'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    qvix_indexs = config.get(cfg_sec, 'qvix_day_indexs').split(',')
    # up_date = config.get(cfg_sec, 'update_date')
    main_period = int(config.get(cfg_sec, 'qvix_day_main_period'))
    all_periods = config.get(cfg_sec, 'qvix_day_periods')
    all_prds = [int(a.strip()) for a in all_periods.split(',')]

    qvix_sta_lines = list()
    qvix_doc_dict = {'qvix_day_periods':all_periods}
    for sym in qvix_indexs:
        img_pth = os.path.join('../data_save', config.get('Basic_Info','doc_img_pth'),'qvix_day_{}_per.png'.format(sym))
        q_pd = make_qvix_macd_smooth(sym,main_w=main_period,winds=all_prds)
        q_tl = make_qvix_day_tline(sym,all_prds,dict(q_pd.iloc[-1]))
        qvix_sta_lines.append(q_tl)
        make_qvix_day_plt(q_pd,img_pth,sym,smooth_wind=main_period)
        qvix_doc_dict.update({
            'qvix_day_{}_tlst'.format(sym):q_tl[1:],
            'qvix_day_{}_ppth'.format(sym):os.path.abspath(img_pth)
        })
        qvix_doc_dict['qvix_day_date'] = q_pd.index[-1].date()
    qvix_doc_dict['qvix_day_tlst'] = '\n'.join(qvix_sta_lines)
    # print(qvix_doc_dict)
    return qvix_doc_dict

if __name__=='__main__':
    # append_qvix_minute_file()
    append_qvix_day_file()
    # make_qvix_day_plt(make_qvix_macd_smooth(),'../data_save/300.png')
    # option_call_put_positon(option_qvix('50'),'510050')
    # make_option_day_pds()
    pass