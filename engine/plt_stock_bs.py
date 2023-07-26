import matplotlib.pyplot as plt
import akshare as ak
import pandas as pd
import numpy as np
import mplfinance as mpf
import os
from common.smooth_tool import log_min_max_dist_ser, min_max_dist_pd

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


def get_index_ohlc(idx_name,beg,end):
    df = ak.index_zh_a_hist(idx_name,start_date=beg,end_date=end)
    df.set_index('日期',inplace=True)
    df.index.name = 'date'
    return df


def plt_index_with_tjy(index_name, zdf, beg, end):
    ''' 添加指标信息并绘图 '''
    index_df = get_index_ohlc(index_name,'2017-01-01','2023-07-21')
    ndf = pd.concat([index_df,zdf],axis=1,join='inner')
    ndf.rename({'开盘':'Open','收盘':'Close','最高':'High','最低':'Low'},
            axis=1,inplace=True)
    ndf.index = pd.to_datetime(ndf.index)
    bsP = mark_up_down(ndf)
    add_plot = [mpf.make_addplot(bsP.loc[beg:end,cl],scatter=True, type='scatter',**mark_dic(cl)) for cl in bsP.columns]
    ndf['long_period'] = [x if x<=20 else np.nan for x in ndf.loc[:,'长周期指数']]
    ndf['stg'] = [x if x>=60 else np.nan for x in ndf.loc[:,'强弱指数']]
    add_plot.append(mpf.make_addplot(ndf.loc[beg:end,'long_period'],panel=1,color='b', secondary_y='auto'))
    add_plot.append(mpf.make_addplot(ndf.loc[beg:end,'stg'],panel=2,color='tomato', secondary_y='auto'))
    if not any(ndf.loc[:,'顶部指数'].isna()):
        add_plot.append(mpf.make_addplot(ndf.loc[beg:end,'底部指数'],panel=3,color='maroon', secondary_y='auto'))
        add_plot.append(mpf.make_addplot(ndf.loc[beg:end,'顶部指数'],panel=3,color='navy', secondary_y='auto'))
    # return add_plot
    add_plot = [a for a in add_plot if not a['data'].isna().all()]
    mpf.plot(ndf.loc[beg:end],type='candle',style=stl, addplot=add_plot, ylabel='price',title='SH.'+index_name,volume=False, figratio=(6,5),
             ylabel_lower='Volume')

def get_stock_df(idx_l=idx_lst[0],bword='牛市',beg='2018-06-01',end='2019-04-30'):
    # slim_date = ('2017-10','2018-06')
    if 2<=len(idx_l)<=3 and idx_l[-1]=='0':
        df = ak.futures_main_sina(idx_l,start_date='20160201',end_date='20230721')
        df.rename(columns={'日期':'date','开盘价':'Open','收盘价':'Close', '最高价':'High', '最低价':'Low'},inplace=True)
    else:
        df = ak.index_zh_a_hist(idx_l,start_date='20160201',end_date='20230721')
        df.rename({'日期':'date','开盘':'Open','收盘':'Close','最高':'High','最低':'Low'},axis=1,inplace=True)
    df.set_index('date',inplace=True)
    df.index = [x.strftime('%Y-%m-%d') for x in df.index]
    bsearch = pd.read_csv('../data_save/bsearch_day.csv',index_col=0)
    if isinstance(bword,str): bword = [bword]
    for b in bword:
        bsplit = bsearch[bsearch['keyword']==b][['count']]
        bsplit.rename(columns={'count':b},inplace=True)
        df = pd.concat([df,bsplit],axis=1,join='inner')
        df['Q_'+b] = log_min_max_dist_ser(bsplit[b],120)
    # df['Volume'] /= 1e8
    df.index = pd.to_datetime(df.index)
    bsP = mark_up_down(df)
    # return bsP
    add_plot = [mpf.make_addplot(bsP.loc[beg:end,cl],
                    scatter=True, type='scatter',**mark_dic(cl)) for cl in bsP.columns]
    for i,b in enumerate(bword):
        add_plot.append(mpf.make_addplot(df.loc[beg:end,b],type='bar', panel=i+1, width=0.7, color='darkgray', secondary_y=False,ylabel=b))
        add_plot.append(mpf.make_addplot(df.loc[beg:end,'Q_'+b], panel=i+1, linewidths=0.7, color='tomato',secondary_y=True))
    add_plot = [a for a in add_plot if not a['data'].isna().all()]
    mpf.plot(df.loc[beg:end],type='candle',
             style=stl, addplot=add_plot, ylabel='price',datetime_format='%m-%d',xrotation=15,
             title='SH.'+idx_l,figratio=(6,5))

# get_stock_df('000001',('股市','上证指数','a股','牛市','熊市'), '2023-02-01','2023-05-21')
# get_stock_df('RB0','螺纹钢', '2022-02-01','2022-11-21')
# plt.grid(True)