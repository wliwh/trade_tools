import configparser
import os
import numpy as np
import pandas as pd
import akshare as ak
from string import ascii_uppercase
os.chdir(os.path.dirname(__file__))
from common.trade_date import get_trade_day


Basic_Funds_CNI = [
    'H11021',   # stk
    '930890',
    '930950',   # part
    '932055'    # act-part
]

def find_index_propline(p:pd.Series, tms:list, ann_day:int=243):
    prop_col = dict()
    plines, lidx = list(), set()
    for y in tms:
        if isinstance(y, str) and len(y)==2: y='20'+y
        _min_col = p[p==p[f'{y}-01-01':].min()]
        # if _min_col.empty: continue
        _dt, _val = _min_col.index[0], _min_col.values[0]
        _loc = p.index.get_loc(_dt)
        if _val not in lidx:
            lidx.add(_val)
            plines.append([_loc,_dt,_val])
    N = len(plines)
    for i in range(N-1):
        _i1,_d1,_p1 = plines[i]
        _i2,_d2,_p2 = plines[i+1]
        _ann = pow(_p2/_p1,ann_day/(_i2-_i1))
        prop_col[f'low{i+1}'] = _d1
        prop_col[f'ann{i+1}'] = _ann
        prop_col['ann'+ascii_uppercase[i]] = '{:.2f}\%'.format(100*(_ann-1))
    prop_col[f'low{N}'] = plines[N-1][1]
    prop_col[f'nValue'] = plines[N-1][2]
    prop_col['CNT'] = N
    return prop_col

def get_basic_funds_index(funds_cni:list=Basic_Funds_CNI,
                          date_lst:list=[2008,2012,2018],
                          cfg_file:str=''):
    pworks = dict()
    if not cfg_file:
        cfg_file = '../trade.ini'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get('Funds_Index', 'fpath'))
    p1 = pd.read_csv(fpth,index_col=0)
    for bc in funds_cni:
        prop = find_index_propline(p1.loc[p1.code==bc,'close'], date_lst)
        pworks[bc] = prop
    return pworks

def get_near_funds_index(funds_cni:list=Basic_Funds_CNI,ann_day:int=243):
    near_idx = dict()
    tdate = get_trade_day().strftime('%Y%m%d')
    for bc in funds_cni:
        pL = ak.stock_zh_index_hist_csindex(symbol=bc, start_date="20180101", end_date=tdate)[['日期','收盘']]
        lowC1 = pL[pL.iloc[:,1]==pL.iloc[:,1].min()]
        lowC2 = pL[pL.iloc[:,1]==pL.iloc[-500:,1].min()]
        _i1,(_d1,_v1)  = lowC1.index[0], lowC1.values[0]
        _i2,(_d2,_v2)  = lowC2.index[0], lowC2.values[0]
        _ann = pow(_v2/_v1, ann_day/(_i2-_i1))
        near_idx[bc] = dict(low=_d2.strftime('%Y-%m-%d'),
                            ann=_ann,
                            Value=_v2,
                            shift=_i2-_i1)
    return near_idx

def all_funds_propline(funds_cni:list = Basic_Funds_CNI,
                       date_lst:list = [2008, 2012, 2018],
                       ann_day:int=243):
    binfo = get_basic_funds_index(funds_cni,date_lst)
    ninfo = get_near_funds_index(funds_cni, ann_day)
    _max_cnt = max(binfo[bc]['CNT'] for bc in funds_cni)
    tab_cols = ['ann'+ascii_uppercase[i] for i in range(_max_cnt)] + \
               [f'low{i+1}' for i in range(_max_cnt+1)] + ['expect_pct']
    for bc in funds_cni:
        cnt = binfo[bc]['CNT']
        _bans = [binfo[bc][f'ann{i}'] for i in range(1,cnt)]
        _min_an, _max_an = np.min(_bans), np.max(_bans)
        _ex_val =  [binfo[bc]['nValue'] * pow(k,(ninfo[bc]['shift'])/ann_day) for k in (_min_an, _max_an)]
        _ex_val = ['{:.2f}%'.format(100*(e/ninfo[bc]['Value']-1)) for e in _ex_val]
        _ann = ninfo[bc]['ann']
        _low = ninfo[bc]['low']
        _annX = '{:.2f}\%'.format(100*(_ann-1))
        if _ann>_max_an:
            _low = '({})'.format(_low); _annX = '({})'.format(_annX)
        binfo[bc][f'low{cnt+1}'] = _low
        binfo[bc][f'ann{cnt-1}'] = _ann
        binfo[bc]['ann'+ascii_uppercase[cnt-1]] = _annX
        binfo[bc]['expect_pct'] = ', '.join(_ex_val)
    btab = pd.DataFrame(binfo).transpose()
    btab = btab[tab_cols]
    return btab

print(get_basic_funds_index(Basic_Funds_CNI))
# print(all_funds_propline())