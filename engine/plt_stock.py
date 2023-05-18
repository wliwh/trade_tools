import matplotlib.pyplot as plt
import akshare as ak
import pandas as pd
import numpy as np
import mplfinance as mpf
import os
from common.smooth_tool import log_min_max_dist_pd, min_max_dist_pd

os.chdir(os.path.dirname(__file__))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

idx_lst = '000001 000016 000300 000852'.split()

mark_col = mpf.make_marketcolors(
    up="red",  # 上涨K线的颜色
    down="green",  # 下跌K线的颜色
    edge="black",  # 蜡烛图箱体的颜色
    volume="inherit",  # 成交量柱子的颜色
    wick="black"  # 蜡烛图影线的颜色
)

stl = mpf.make_mpf_style(
    gridaxis='both',
    gridstyle='-.',
    y_on_right=False,
    marketcolors=mark_col,
    rc={'font.family': 'SimHei', 'axes.unicode_minus': 'False'}
    )

def mark_up_down(dts,winds=(20,60,200),price='l/h'):
    ''' 添加买卖点 '''
    def parse_price(tb,i,price=price):
        if price.lower()=='l/h':
            if tb.iloc[i]['Low']<=min(tb['Low']):
                return 'B', tb.iloc[i]['Low']-20
            elif tb.iloc[i]['High']>=max(tb['High']):
                return 'S', tb.iloc[i]['High']+20
            return
        elif price.lower()=='c':
            if tb.iloc[i]['Close']<=min(tb['Close']):
                return 'B', tb.iloc[i]['Low']-20
            elif tb.iloc[i]['Close']>=max(tb['Close']):
                return 'S', tb.iloc[i]['High']+20
            return
        elif price.lower() in ('co','oc'):
            nval = tb.iloc[i]['Close']+tb.iloc[i]['Open']
            if nval<=min(tb['Close']+tb['Open']):
                return 'B', tb.iloc[i]['Low']-20
            elif nval>=max(tb['Close']+tb['Open']):
                return 'S', tb.iloc[i]['High']+20
            return
        elif price.lower() in ('c/o','o/c'):
            nval = min(tb.iloc[i]['Close'],tb.iloc[i]['Open'])
            mval = max(tb.iloc[i]['Close'],tb.iloc[i]['Open'])
            if nval<=tb[['Close','Open']].values.min():
                return 'B', tb.iloc[i]['Low']-20
            elif mval>=tb[['Close','Open']].values.max():
                return 'S', tb.iloc[i]['High']+20
            return
        return

    wind_l = list(sorted(winds,reverse=True))
    max_W = max(winds)
    bs_pd = pd.DataFrame(np.zeros((len(dts),len(winds)*4)),index=dts.index,
            columns=['%s_%d' % (n,w) for n in 'BSbs' for w in wind_l])
    bs_pd.loc[:,:] = np.nan
    for w in wind_l:
        for i in range(w,len(dts)):
            if i<len(dts)-w:
                nval = parse_price(dts.iloc[i-w:i+w+1],w,price)
            else:
                nval = parse_price(dts.iloc[i-w:],w,price)
                if nval: nval = (nval[0].lower(), nval[1])
            if nval and (bs_pd.iloc[i][nval[0]+'_'+str(max_W):nval[0]+'_'+str(w)].isna().all()):
                bs_pd.iloc[i][nval[0]+'_'+str(w)] = nval[1]
    return bs_pd

def mark_dic(cl_n):
    cl_sz = {'20':50,'60':100,'200':150}
    p1, pcl = ('^','r') if cl_n[0].lower()=='b' else ('v','g')
    alp = 0.5 if cl_n[0].islower() else 1
    return {'markersize':cl_sz[cl_n[2:]], 
            'marker': p1, 'color': pcl, 'alpha':alp}

def get_stock_df(idx_l=idx_lst[0],bword='a股'):
    slim_date = ('2022-11','2023-05')
    df = ak.index_zh_a_hist(idx_l,start_date='20170201',end_date='20230501')
    df.set_index('日期',inplace=True)
    df.index.name = 'date'
    bsearch = pd.read_csv('../data_save/bsearch_day.csv',index_col=0)
    bsearch = bsearch[bsearch['keyword']==bword][['count']]
    df = pd.concat([df,bsearch],axis=1,join='inner')
    df['Volume'] = df['count']
    df['Qsearch'] = log_min_max_dist_pd(bsearch,60,'count')
    df.rename({'开盘':'Open','收盘':'Close',
            '最高':'High','最低':'Low'},
            axis=1,inplace=True)
    # df['Volume'] /= 1e8
    df.index = pd.to_datetime(df.index)
    bsP = mark_up_down(df)
    add_plot = [mpf.make_addplot(bsP.loc[slim_date[0]:slim_date[1],cl],
                    scatter=True, type='scatter',**mark_dic(cl)) for cl in bsP.columns]
    add_plot.append(mpf.make_addplot(df.loc[slim_date[0]:slim_date[1],'Qsearch'],panel='lower',color='b', secondary_y='auto'))
    add_plot = [a for a in add_plot if not a['data'].isna().all()]
    mpf.plot(df.loc[slim_date[0]:slim_date[1]],type='candle',
             style=stl, addplot=add_plot, ylabel='price',
             title='SH.'+idx_l,volume=True, figratio=(6,3),
             ylabel_lower='Volume')

get_stock_df(bword='a股')
# plt.grid(True)