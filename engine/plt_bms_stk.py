import pandas as pd
import numpy as np
import efinance as ef
import os
import os.path as osp
import zigzag
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as dates
from common.trade_date import get_delta_trade_day

Kline_Min_Dir = osp.join(osp.dirname(__file__),'../kmin')
Kline_Min_Pth = [osp.join(Kline_Min_Dir,p)
        for p in os.listdir(Kline_Min_Dir)
            if p.endswith('csv')]
BMS_Index_Name = ('上证50','沪深300','中证500',
        '中证1000','国证2000','国证A指')
Index_CMap = dict(
    up=dict(
        上证50='#7c1823',       # 枣红
        沪深300='#f04b22',      # 大红
        中证500='#f9723d',      # 芙蓉红
        中证1000='#f19790',     # 舌红
        国证2000='#f2cac9',     # 淡绯
        国证A指='#e3ac05'
    ),
    down=dict(
        上证50='#5e665b',       # 田螺绿
        沪深300='#20894d',      # 宫殿绿
        中证500='#43b244',      # 鲜绿
        中证1000='#8cc269',     # 水绿
        国证2000='#c6dfc8',     # 淡翠绿
        国证A指='#e3ac05'
    ),
    pts=dict(
        上证50='#879596',
        沪深300='#9ba6a8',
        中证500='#afb8b9',
        中证1000='#c3caca',
        国证2000='#d7dbdc',
        国证A指='#e3ac05'
    )
)
Index_Ticks = [5,24,60,238]

def calc_index_pct(pth:str, dt:str):
    ''' 计算分钟级涨跌 '''
    p1 = pd.read_csv(pth,index_col=0)
    tmp = p1.loc[p1.index.map(lambda x:x[:10]==dt)]
    incs = (tmp['close']/tmp['pdclose']-1).values
    if dt+' 14:59:00' not in tmp.index:
        return np.insert(incs,-1,incs[-2])
    else:
        return incs

def arange_bms_index_min(dt:str,
                idx_name:tuple=BMS_Index_Name,
                idx_pths:list=Kline_Min_Pth)->pd.DataFrame:
    ''' 大小指数的分钟图涨跌计算 '''
    bms_min_tb = pd.DataFrame([],columns=idx_name,
                              index=range(1,241))
    kline_name = [osp.basename(p) for p in idx_pths]
    for nm in idx_name:
        knth = kline_name.index(nm+'.csv') if nm+'.csv'\
            in kline_name else None
        if knth is None: continue
        kpth = idx_pths[knth]
        bms_min_tb[nm] = calc_index_pct(kpth,dt)
    return bms_min_tb*100.0

def plt_bms_index_min(bms_tb:pd.DataFrame,
                      idx_name:tuple=BMS_Index_Name,
                      cm:dict=Index_CMap):
    ccm = cm['up']
    if bms_tb.loc[240].mean()<-0.5: ccm = cm['down']
    plt.xscale('log',base=5)
    for nm in idx_name:
        plt.plot(bms_tb[nm],color=ccm[nm])
        plt.scatter(Index_Ticks,bms_tb.loc[Index_Ticks,nm],
                    color=ccm[nm]) # cm['pts'][nm])
    plt.legend()
    plt.show()


def find_zigs(code:str,pct:int,beg:str,end:str):
    p1 = ef.stock.get_quote_history(code,beg.replace('-',''),end.replace('-',''),fqt=0)
    p1.columns = ('name','code','date','o','h','l','c','amt','vol','zf','inc','pct','hs')
    p1.set_index('date',inplace=True)
    while pct>=2:
        wpct = pct/100
        res = zigzag.peak_valley_pivots_detailed(p1.loc[beg:end,'c'].values,wpct,-wpct,False,False)
        lidx, hidx = np.where(res==-1)[0], np.where(res==1)[0]
        if lidx.size>=1 and hidx.size>=2:
            break
        if pct==2: break
        pct -= 1
    # return pct, res
    if 0 in hidx:
        bd1_dt = (lidx[0],hidx[1])
        bd1_inc = (p1.iloc[bd1_dt[0]]['c'],p1.iloc[bd1_dt[1]]['c'])
    else:
        bd1_dt = (lidx[0], hidx[0])
        bd1_inc = (p1.iloc[bd1_dt[0]]['c'],p1.iloc[bd1_dt[1]]['c'])
        if bd1_inc[1]/bd1_inc[0]*100<max(100+pct,102):
            try:
                bd1_dt = (lidx[1], hidx[1])
            except IndexError as e:
                next_day = get_delta_trade_day(end,1).strftime('%Y-%m-%d')
                return find_zigs(code,pct,beg,next_day)
            bd1_inc = (p1.iloc[bd1_dt[0]]['c'],p1.iloc[bd1_dt[1]]['c'])
    return dict(beg=p1.iloc[bd1_dt[0]].name,
                end=p1.iloc[bd1_dt[1]].name,
                days=bd1_dt[1]-bd1_dt[0],
                low=bd1_inc[0],
                high=bd1_inc[1],
                inc=bd1_inc[1]/bd1_inc[0]*100-100)

# plt_bms_index_min(arange_bms_index_min('2023-10-19'))

print(find_zigs('399317',5,'2023-05-05','2023-06-26'))