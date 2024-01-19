import configparser
import os
import numpy as np
import pandas as pd
import akshare as ak
from string import ascii_uppercase
os.chdir(os.path.dirname(__file__))
from common.trade_date import get_trade_day,get_delta_trade_day


Basic_Funds_CNI = [
    'H11021',   # stk
    '930890',
    '930950',   # part
    '932055'    # act-part
]

def get_funds_index(cfg_file:str=''):
    if not cfg_file:
        cfg_file = '../trade.ini'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get('Funds_Index', 'fpath'))
    p1 = pd.read_csv(fpth,index_col=0)
    return p1

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
        if i==0: prop_col['idxA'] = _i1; prop_col['idxB'] = _i2
        elif i==N-2: prop_col['idxC'] = _i1; prop_col['idxD'] = _i2
        _ann = pow(_p2/_p1,ann_day/(_i2-_i1))
        prop_col[f'low{i+1}'] = _d1
        prop_col[f'ann{i+1}'] = _ann
        prop_col['ann'+ascii_uppercase[i]] = '{:.2f}\%'.format(100*(_ann-1))
    prop_col[f'low{N}'] = plines[N-1][1]
    prop_col[f'nValue'] = plines[N-1][2]
    prop_col['CNT'] = N
    return prop_col

def get_basic_funds_prop(funds_cni:list=Basic_Funds_CNI,
                          date_lst:list=[2008,2012,2018],
                          cfg_file:str=''):
    pworks = dict()
    p1 = get_funds_index(cfg_file)
    for bc in funds_cni:
        prop = find_index_propline(p1.loc[p1.code==bc,'close'], date_lst)
        pworks[bc] = prop
    return pworks

def calc_funds_prop(funds_cni:list=Basic_Funds_CNI,
                    date_lst:list=[2008,2012,2018],
                    cfg_file:str=''):
    code_prop = dict()
    tdate = get_trade_day().strftime('%Y%m%d')
    p1 = get_funds_index(cfg_file)
    for bc in funds_cni:
        tmp = p1.loc[p1.code==bc,['close']]
        beg_d = get_delta_trade_day(tmp.index[-1],1).strftime('%Y%m%d')
        pL = ak.stock_zh_index_hist_csindex(symbol=bc, start_date=beg_d, end_date=tdate)[['日期','收盘']]
        pL.columns = ('date','close')
        pL.set_index('date',inplace=True)
        pL.index = pL.index.map(lambda x:x.strftime('%Y-%m-%d'))
        tmp = pd.concat([tmp,pL],axis=0)
        tmp['evalue'] = np.nan
        prop = find_index_propline(tmp['close'], date_lst)
        for r in range(prop['CNT']):
            tmp.loc[prop[f'low{r+1}'],'evalue'] = tmp.loc[prop[f'low{r+1}'],'close']
        i1,i2,i3,i4 = prop['idxA'],prop['idxB'],prop['idxC'],prop['idxD']
        tmp['evalue'] = np.log(tmp['evalue'])
        tmp.iloc[0,1] = tmp.iloc[i1,1] - (tmp.iloc[i2,1]-tmp.iloc[i1,1]) * i1/(i2-i1)
        tmp.iloc[-1,1] = tmp.iloc[i4,1] + (tmp.iloc[i4,1]-tmp.iloc[i3,1])*(len(tmp)-1-i4)/(i4-i3)
        tmp['evalue'].interpolate(method='linear',inplace=True)
        tmp['evalue'] = np.exp(tmp['evalue'])
            # print(tmp.loc[prop[f'low{r+1}'],'close'])
        return tmp
    
# print(calc_funds_prop(Basic_Funds_CNI[2:]))

def get_near_funds_prop(funds_cni:list=Basic_Funds_CNI,ann_day:int=243):
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
    ''' 生成基金指数的支撑线和推测值 '''
    binfo = get_basic_funds_prop(funds_cni,date_lst)
    ninfo = get_near_funds_prop(funds_cni, ann_day)
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

# print(get_basic_funds_prop(Basic_Funds_CNI))
print(all_funds_propline())