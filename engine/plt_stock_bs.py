import matplotlib.pyplot as plt
import akshare as ak
import pandas as pd
import numpy as np
import mplfinance as mpf
import os
from pyecharts import options as opts
from pyecharts.charts import Kline, Bar, Grid
from common.smooth_tool import log_min_max_dist_ser, super_smoother, LLT_MA
from common.mpf_set import Mpf_Style

os.chdir(os.path.dirname(__file__))
bd_pth = os.path.abspath('../data_save/bsearch_day.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

idx_dct = {'上证综指':'000001',
           '上证50':'000016',
           '沪深300':'000300',
           '中证1000':'000852',
           '中证全指':'000985'}

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


def get_index_ohlc(idx_l,beg,end):
    if 2<=len(idx_l)<=3 and idx_l[-1]=='0':
        df = ak.futures_main_sina(idx_l,start_date=beg,end_date=end)
        df.rename(columns={'日期':'date','开盘价':'Open','收盘价':'Close', '最高价':'High', '最低价':'Low','成交量':'Volume'},inplace=True)
        df['Volume'] /= 1e6
    else:
        df = ak.index_zh_a_hist(idx_l,start_date=beg,end_date=end)
        df.rename({'日期':'date','开盘':'Open','收盘':'Close','最高':'High','最低':'Low','成交量':'Volume'},axis=1,inplace=True)
        df['Volume'] /= 1e8
    df.set_index('date',inplace=True)
    if not isinstance(df.index[0],str):
        df.index = [x.strftime('%Y-%m-%d') for x in df.index]
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
    mpf.plot(ndf.loc[beg:end],type='candle',style=Mpf_Style, addplot=add_plot, ylabel='price',title='SH.'+index_name,volume=False, figratio=(6,5),
             ylabel_lower='Volume')

def get_stock_bdkey(idx_l:str,bword='牛市',beg='2018-06-01',end='2019-04-30'):
    # slim_date = ('2017-10','2018-06')
    df = get_index_ohlc(idx_l,'2016-01-01',end=end)
    bsearch = pd.read_csv(bd_pth,index_col=0)
    if isinstance(bword,str): bword = [bword]
    tps = idx_l+bword[0]+beg[2:].replace('-','')+'.png'
    for b in bword:
        bsplit = bsearch[bsearch['keyword']==b][['count']]
        bsplit.rename(columns={'count':b},inplace=True)
        df = pd.concat([df,bsplit],axis=1,join='inner')
        df['Q_'+b] = log_min_max_dist_ser(bsplit[b],120)
        df['diff_'+b] = bsplit[b] - super_smoother(bsplit[b],20)
    df.index = pd.to_datetime(df.index)
    bsP = mark_up_down(df)
    add_plot = [mpf.make_addplot(bsP.loc[beg:end,cl],
                    scatter=True, type='scatter',**mark_dic(cl)) for cl in bsP.columns]
    for i,b in enumerate(bword):
        add_plot.append(mpf.make_addplot(df.loc[beg:end,b],type='bar', panel=i*2+2, width=0.7, color='darkgray', secondary_y=False,ylabel=b))
        add_plot.append(mpf.make_addplot(df.loc[beg:end,'Q_'+b], panel=i*2+2, width=0.8, color='tomato',secondary_y=True))
        add_plot.append(mpf.make_addplot(df.loc[beg:end,'diff_'+b],panel=i*2+3,width=0.6, color='darkblue',ylabel='Diff'))
    add_plot = [a for a in add_plot if not a['data'].isna().all()]
    mpf.plot(df.loc[beg:end],type='candle',
             style=Mpf_Style, addplot=add_plot, ylabel='price',
             savefig={'fname':'./img/'+tps,'dpi':400,'bbox_inches':'tight'},
             datetime_format='%m-%d',xrotation=15,volume=True,
             title=idx_l,figratio=(10,max(10,len(bword)*3)))
    

def make_stk_plts(idx_l:str):
    date_lst = (('2017-10-10','2018-04-10'),
                ('2018-03-20','2018-09-10'),
                ('2018-09-01','2019-02-10'),
                ('2021-11-01','2022-05-20'),
                ('2022-05-01','2022-12-10'))
    for d in date_lst:
        get_stock_bdkey('000001',('股市','上证指数','a股'), d[0],d[1])
        get_stock_bdkey('000001',('牛市','熊市'), d[0],d[1])
        get_stock_bdkey('000300',('沪深300','上证50','a股'), d[0],d[1])
        get_stock_bdkey('399006',('创业板指','a股'), d[0],d[1])


def make_echarts(idx_l:str,bword='牛市',beg='2018-06-01',end='2019-04-30'):
    df = get_index_ohlc(idx_l,'2016-01-01',end=end)
    data = df.loc[beg:,:'Low']
    volume_ser = df.loc[beg:,'Volume']
    bsearch = pd.read_csv(bd_pth,index_col=0)
    kline = (
        Kline(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add_xaxis([d for d in data.index])
        .add_yaxis("kline", data.values.tolist())
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            datazoom_opts=[opts.DataZoomOpts(pos_bottom="2%")],
            title_opts=opts.TitleOpts(title="Kline-DataZoom-slider-Position"),
        )
    )
    bar = (
        Bar()
            .add_xaxis(xaxis_data=list(data.index))  # X轴数据
            .add_yaxis(
            series_name="volume",
            y_axis=volume_ser.tolist(),  # Y轴数据
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(color='#ef232a'  # '#14b143'
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",  # 坐标轴类型-离散数据
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    # 图像排列
    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="1200px",  # 显示图形宽度
            height="800px",
            animation_opts=opts.AnimationOpts(animation=False),  # 关闭动画
        )
    )

    grid_chart.add(  # 加入均线图
        kline,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height="50%"),
    )
    grid_chart.add(  # 加入成交量图
        bar,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top="60%", height="20%"),
    )
    grid_chart.render("大量数据展示.html")



if __name__=='__main__':
    # get_stock_bdkey('000001',('股市','上证指数','a股'), '2022-06-20','2022-12-31')
    # get_stock_bdkey('000001',('牛市','熊市'), '2022-06-20','2022-12-31')
    # get_stock_bdkey('RB0','螺纹钢', '2023-03-01','2023-07-21')
    # print(get_index_ohlc('RB0','2022-02-01','2022-05-01'))
    # plt.grid(True)
    # make_stk_plts(0)
    make_echarts('000001')
    pass