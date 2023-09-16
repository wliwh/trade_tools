import matplotlib.pyplot as plt
import akshare as ak
import pandas as pd
import numpy as np
import mplfinance as mpf
import os
from pyecharts import options as opts
from pyecharts.charts import Kline, Bar, Grid, Line, Tab
from pyecharts.commons.utils import JsCode
from common.smooth_tool import min_max_dist_series, super_smoother, LLT_MA
from common.mpf_set import Mpf_Style
from data_cper.funds_positions import make_margin_concat_pd

os.chdir(os.path.dirname(__file__))
BD_PTH = os.path.abspath('../data_save/bsearch_day.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

IDX_DCT = {'上证综指':'000001',
           '上证50':'000016',
           '沪深300':'000300',
           '中证1000':'000852',
           '创业板指': '399006',
           '中证全指':'000985',
           '螺纹钢':'RB0',
           '生猪':'lh0',
           '原油':'sc0'}

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
    ''' 获取index基本表格 '''
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

def get_index_with_bsearch(idx_l:str, bword, end:str,**kwargs):
    df = get_index_ohlc(idx_l,'2016-01-01',end=end)
    bsearch = pd.read_csv(BD_PTH,index_col=0)
    bd_mm_dist = kwargs.get('dist_day',120)
    ssmooth_day = kwargs.get('ssmooth_day',20)
    llt_day = kwargs.get('llt_ma',14)
    qz_dst = kwargs.get('calc_qz',(0.6,0.4))
    if isinstance(bword,str): bword = [bword]
    for b in bword:
        bsplit = bsearch[bsearch['keyword']==b][['count']]
        bsplit.rename(columns={'count':b},inplace=True)
        df = pd.concat([df,bsplit],axis=1,join='inner')
        df['Q_'+b] = min_max_dist_series(bsplit[b],bd_mm_dist)
        df['diff_'+b] = bsplit[b] - 0.5*super_smoother(bsplit[b],ssmooth_day)-0.5*LLT_MA(bsplit[b],1/llt_day)
        df['diffQ_'+b] = min_max_dist_series(df['diff_'+b],bd_mm_dist)
        df['CalcQ_'+b] = qz_dst[0]*df['Q_'+b]+qz_dst[1]*df['diffQ_'+b]
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
    if isinstance(bword,str): bword = [bword]
    df = get_index_with_bsearch(idx_l,bword,end)
    df.index = pd.to_datetime(df.index)
    bsP = mark_up_down(df)
    tps = idx_l+bword[0]+beg[2:].replace('-','')+'.png'
    add_plot = [mpf.make_addplot(bsP.loc[beg:end,cl],
                    scatter=True, type='scatter',**mark_dic(cl)) for cl in bsP.columns]
    for i,b in enumerate(bword):
        add_plot.append(mpf.make_addplot(df.loc[beg:end,b],type='bar', panel=i*2+2, width=0.7, color='darkgray', secondary_y=False,ylabel=b))
        add_plot.append(mpf.make_addplot(df.loc[beg:end,'Q_'+b], panel=i*2+2, width=0.8, color='tomato',secondary_y=True))
        add_plot.append(mpf.make_addplot(df.loc[beg:end,'diff_'+b],panel=i*2+3,width=0.6, color='darkblue',ylabel='Diff'))
        add_plot.append(mpf.make_addplot(df.loc[beg:end,'llt_'+b],panel=i*2+3,width=0.6, color='tomato',ylabel='Diff'))
    add_plot = [a for a in add_plot if not a['data'].isna().all()]
    mpf.plot(df.loc[beg:end],type='candle',
             style=Mpf_Style, addplot=add_plot, ylabel='price',
            #  savefig={'fname':'./img/'+tps,'dpi':400,'bbox_inches':'tight'},
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


def _get_windA_mins(p1:pd.DataFrame,annual_day=243):
    ylst = ('2005','2008', '2013','2019','2022','2023')
    pairs = ((0,2),(1,2),(2,3),(3,4),(4,5))
    plst = list()
    prs = list()
    for y in ylst:
        ls = p1[p1['Low']==p1.loc[y+'-01-01':y+'-12-31','Low'].min()]
        plst.append(ls.index[0])
    for i1,i2 in pairs:
        d1,d2 = plst[i1],plst[i2]
        ddt = p1.index.get_loc(d2) - p1.index.get_loc(d1)
        low1, low2 = p1.loc[d1,'Low'], p1.loc[d2,'Low']
        ann_inc = np.power(low2/low1,annual_day/ddt)
        prs.append((d1,d2,low1,low2,ann_inc))
    return prs

def make_windA_echarts(beg='2011-06-01',end='2023-08-22',annual_inc=1.1):
    wa = pd.read_csv('../data_save/windA.csv',index_col=0)
    wa.sort_index(inplace=True)
    wa.columns = ['Open','High','Low','Close','Exc','Pct','Volume','Amount']
    wa.index.name = 'date'
    _plt_range_len = 120
    _annual_day = 243
    inctb = _get_windA_mins(wa,_annual_day)
    _base_day = '2018-10-19' # '2019-01-04' '2022-04-27' '2022-10-31'
    _base_point = wa.loc[_base_day,'Low']
    _base_idx = wa.index.get_loc(_base_day)
    wa['bline'] = _base_point
    for i,d in enumerate(wa.index):
        if i>_base_idx:
            wa.loc[d,'bline'] = _base_point*np.power(1.09,(i-_base_idx)/_annual_day)
        else:
            wa.loc[d,'bline'] = _base_point*np.power(annual_inc,(i-_base_idx)/_annual_day)

    data = wa.loc[beg:end,['Open','Close','Low','High']]
    volume_ser = wa.loc[beg:end,'Volume']
    bline = wa.loc[beg:end,'bline']
    _range_len = int((_plt_range_len*100)/len(data))
    _range_len = 90 if _range_len>100 else _range_len
    _datazoom_opt = [
        opts.DataZoomOpts(is_show=False, type_="inside", 
                            xaxis_index=[0, 0], range_start=100-_range_len,range_end=100),
        opts.DataZoomOpts(is_show=True, pos_bottom="2%",
                            range_start=100-_range_len,
                            xaxis_index=[0, 1], range_end=100)
    ]
    kline = (
        Kline()
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
            datazoom_opts=_datazoom_opt,
            title_opts=opts.TitleOpts(title="万得全A"),
        )
    )
    base_line = (
        Line()
        .add_xaxis(xaxis_data=data.index.tolist())
        .add_yaxis(
            series_name="base_line",
            y_axis=bline,
            is_smooth=True,
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=1,
                split_number=3,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
        )
    )
    overlap_kline_line = kline.overlap(base_line)
    bar = (
        Bar()
            .add_xaxis(xaxis_data=data.index.tolist())  # X轴数据
            .add_yaxis(
            series_name="vols",
            y_axis=volume_ser.tolist(),  # Y轴数据
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color=JsCode(
                """
                function(params) {
                    var colorList;
                    if (barData[params.dataIndex][1] > barData[params.dataIndex][0]) {
                        colorList = '#ef232a';
                    } else {
                        colorList = '#14b143';
                    }
                    return colorList;
                }
                """
                )
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",  # 坐标轴类型-离散数据
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(position='right'),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="{}px".format(1200),  # 显示图形宽度
            height='750px',
            animation_opts=opts.AnimationOpts(animation=False),  # 关闭动画
        )
    )

    grid_chart.add_js_funcs("var barData = {}".format(data.values.tolist()))
    grid_chart.add(  # 加入均线图
        overlap_kline_line,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height='65%'),
    )
    grid_chart.add(  # 加入成交量图
        bar,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top='75%', height='20%'),
    )
    grid_chart.render('stockWindA.html')


def make_marg_echarts(beg='2017-01-01',end='2023-08-24'):
    dts = get_index_ohlc('399317',beg,end)
    dts.index.name = 'date'
    dts.index = dts.index.map(lambda x:x.replace('-',''))
    dt2 = make_margin_concat_pd('all',pday=1)
    # dt2.index = [x[:4]+'-'+x[4:6]+'-'+x[6:] for x in dt2.index]
    _plt_range_len = 120
    dts = dts.join(dt2)
    # beg, end= '20170101', '20230801'
    data = dts.loc[beg:end,['Open','Close','Low','High']]
    bline = dts.loc[beg:end,'两融差额pct']
    _range_len = int((_plt_range_len*100)/len(data))
    _range_len = 90 if _range_len>100 else _range_len
    _datazoom_opt = [
        opts.DataZoomOpts(is_show=False, type_="inside", 
                            xaxis_index=[0, 0], range_start=100-_range_len,range_end=100),
        opts.DataZoomOpts(is_show=True, pos_bottom="2%",
                            range_start=100-_range_len,
                            xaxis_index=[0, 1], range_end=100),
    ]
    kline = (
        Kline()
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
            datazoom_opts=_datazoom_opt,
            title_opts=opts.TitleOpts(title="国证A指"),
        )
    )
    bar = (
        Bar()
            .add_xaxis(xaxis_data=data.index.tolist())  # X轴数据
            .add_yaxis(
            series_name="两融差值",
            y_axis=bline.abs().tolist(),  # Y轴数据
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color=JsCode(
                """
                function(params) {
                    var colorList;
                    if (barData[params.dataIndex][20] > 0) {
                        colorList = '#ef232a';
                    } else {
                        colorList = '#14b143';
                    }
                    return colorList;
                }
                """
                )
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",  # 坐标轴类型-离散数据
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(position='right'),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="{}px".format(1200),  # 显示图形宽度
            height='750px',
            animation_opts=opts.AnimationOpts(animation=False),  # 关闭动画
        )
    )
    grid_chart.add_js_funcs("var barData = {}".format(dts.loc[beg:end].values.tolist()))
    grid_chart.add(
        kline,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height='65%'),
    )
    grid_chart.add(  # 加入融资变量
        bar,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top='75%', height='20%'),
    )
    grid_chart.render('stockWindA.html')



def make_echarts(idx_l:str,bword='牛市',beg='2018-06-01',end='2019-04-30',**kwargs):
    _plt_range_len = kwargs.get('df_range_len',100)
    _plt_xticks = kwargs.get('plt_xticks',1200)
    def echart_args_get(idx_nm:str, bw:str):
        echart_args = dict(ma_args = (5,10,20,60,120,240))
        if idx_nm in IDX_DCT:
            echart_args['idx_name'] = idx_nm
            echart_args['idx_code'] = IDX_DCT[idx_nm]
        elif idx_nm in IDX_DCT.values():
            echart_args['idx_name'] = {v:k for k,v in IDX_DCT.items()}[idx_nm]
            echart_args['idx_code'] = idx_nm
        else: return None
        if ',' in bw:
            bwl = [a.strip() for a in bw.split(',')]
            assert(len(bwl))==2, 'bword is too long.'
            echart_args.update({
                'bwlen':2, 'bword':bwl,
                'grid':('34%','43%','11%','53%','10%','64%','10%','74%','10%','85%','10%'),
                'qu_pos':('64%','84%'),
                'height':'750px'})
        else:
            echart_args.update({
                'bwlen':1, 'bword':[bw],
                'grid':('45%','55%','13%','68%','12%','82%','10%'),
                'qu_pos':('80%',),
                'height':'700px'})
        return echart_args
    
    echart_dic = echart_args_get(idx_l, bword)
    idx_code = echart_dic['idx_code']
    idx_name = echart_dic['idx_name']
    _bwordl = echart_dic['bword']
    _bwlen = echart_dic['bwlen']
    df = get_index_with_bsearch(idx_code, _bwordl, end=end)
    for d in echart_dic['ma_args']:
        df['ma_'+str(d)] = df['Close'].rolling(d).mean()
    data = df.loc[beg:end,['Open','Close','Low','High']]
    volume_ser = df.loc[beg:end,'Volume']
    _range_len = int((_plt_range_len*100)/len(data))
    _range_len = 90 if _range_len>100 else _range_len
    _datazoom_opt = [
        opts.DataZoomOpts(is_show=False, type_="inside", 
                            xaxis_index=[0, 0], range_start=100-_range_len,range_end=100),
        opts.DataZoomOpts(is_show=True, pos_bottom="2%",
                            range_start=100-_range_len,
                            xaxis_index=[0, 1], range_end=100),
        opts.DataZoomOpts(is_show=False, range_start=100-_range_len,
                            xaxis_index=[0, 2], range_end=100),
        opts.DataZoomOpts(is_show=False, range_start=100-_range_len,
                            xaxis_index=[0, 3], range_end=100)
    ]
    if _bwlen==2:
        _datazoom_opt.extend([
            opts.DataZoomOpts(is_show=False, range_start=100-_range_len,
                                xaxis_index=[0, 4], range_end=100),
            opts.DataZoomOpts(is_show=False, range_start=100-_range_len,
                                xaxis_index=[0, 5], range_end=100)
        ])
    kline = (
        Kline()
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
            datazoom_opts=_datazoom_opt,
            title_opts=opts.TitleOpts(title="{}: {}".format(idx_name,bword)),
        )
    )
    kline_line = (
        Line()
        .add_xaxis(xaxis_data=data.index.tolist())
        .add_yaxis(
            series_name="MA20",
            y_axis=df.loc[beg:end,'ma_'+str(20)],
            is_smooth=True,
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="MA60",
            y_axis=df.loc[beg:end,'ma_60'],
            is_smooth=True,
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=1,
                split_number=3,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
        )
    )
    # Overlap Kline + Line
    overlap_kline_line = kline.overlap(kline_line)
    # volume bar
    bar = (
        Bar()
            .add_xaxis(xaxis_data=data.index.tolist())  # X轴数据
            .add_yaxis(
            series_name="vols",
            y_axis=volume_ser.tolist(),  # Y轴数据
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color=JsCode(
                """
                function(params) {
                    var colorList;
                    if (barData[params.dataIndex][1] > barData[params.dataIndex][0]) {
                        colorList = '#ef232a';
                    } else {
                        colorList = '#14b143';
                    }
                    return colorList;
                }
                """
                )
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",  # 坐标轴类型-离散数据
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(position='right'),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    # bd bar
    bd_bar = (
        Bar()
            .add_xaxis(xaxis_data=data.index.tolist())  # X轴数据
            .add_yaxis(
            series_name=_bwordl[0],
            y_axis= df.loc[beg:end,_bwordl[0]].tolist(),  # Y轴数据
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(color='#bbbbbb'),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=2,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_='value',
                # name='count',
                grid_index=2,
                split_number=3,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    bd_qut_line = (
        Line()
        .add_xaxis(xaxis_data=data.index.tolist())
        # .extend_axis(yaxis=opts.AxisOpts(type_="value", position="right",))
        .add_yaxis(
            series_name="Q120",
            y_axis=df.loc[beg:end,'Q_'+_bwordl[0]].tolist(),
            is_smooth=False,
            # yaxis_index=1,
            symbol_size=2,
            linestyle_opts=opts.LineStyleOpts(opacity=1),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name='ssmooth',
            y_axis=df.loc[beg:end,'diff_'+_bwordl[0]].tolist(),
            is_smooth=False,
            symbol_size = 2,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        # .add_yaxis(
        #     series_name='llt',
        #     y_axis=df.loc[beg:end,'llt_'+_bwordl[0]].tolist(),
        #     is_smooth=False,
        #     is_symbol_show=False,
        #     yaxis_index=1,
        #     label_opts=opts.LabelOpts(is_show=False),
        # )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True,),
                #trigger="axis", axis_pointer_type="cross"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axislabel_opts=opts.LabelOpts(is_show=False)),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                grid_index=3,
                split_number=3,
                position='right',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            legend_opts=opts.LegendOpts(pos_top=echart_dic['qu_pos'][0]),
        )
    )
    if _bwlen==2:
        # bd bar
        bd_bar2 = (
            Bar()
                .add_xaxis(xaxis_data=data.index.tolist())  # X轴数据
                .add_yaxis(
                series_name=_bwordl[1],
                y_axis= df.loc[beg:end,_bwordl[1]].tolist(),  # Y轴数据
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
                itemstyle_opts=opts.ItemStyleOpts(color='#bbbbbb'),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=4,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_='value',
                    grid_index=4,
                    split_number=3,
                    axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                    axislabel_opts=opts.LabelOpts(is_show=True),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )
        bd_qut_line2 = (
            Line()
            .add_xaxis(xaxis_data=data.index.tolist())
            .add_yaxis(
                series_name="Q120",
                y_axis=df.loc[beg:end,'Q_'+_bwordl[1]].tolist(),
                is_smooth=False,
                symbol_size=2,
                linestyle_opts=opts.LineStyleOpts(opacity=1),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name='ssmooth',
                y_axis=df.loc[beg:end,'diff_'+_bwordl[1]].tolist(),
                is_smooth=False,
                symbol_size=2,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
            )
            # .add_yaxis(
            #     series_name='llt',
            #     y_axis=df.loc[beg:end,'llt_'+_bwordl[1]].tolist(),
            #     is_smooth=False,
            #     is_symbol_show=False,
            #     yaxis_index=1,
            #     label_opts=opts.LabelOpts(is_show=False),
            # )
            .set_global_opts(
                tooltip_opts=opts.TooltipOpts(is_show=False,),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axislabel_opts=opts.LabelOpts(is_show=False)),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    grid_index=5,
                    split_number=3,
                    position='right',
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )
    # overlap_bd = bd_bar.overlap(bd_qut_line)
    # 图像排列
    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="{}px".format(_plt_xticks),  # 显示图形宽度
            height=echart_dic['height'],
            animation_opts=opts.AnimationOpts(animation=False),  # 关闭动画
        )
    )

    _g_hts = echart_dic['grid']
    grid_chart.add_js_funcs("var barData = {}".format(data.values.tolist()))
    grid_chart.add(  # 加入均线图
        overlap_kline_line,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height=_g_hts[0]),
    )
    grid_chart.add(  # 加入成交量图
        bar,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top=_g_hts[1], height=_g_hts[2]),
    )
    grid_chart.add(  # 加入关键词量图
        bd_bar,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top=_g_hts[3], height=_g_hts[4]),
    )
    grid_chart.add(  # 加入关键词量图
        bd_qut_line,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top=_g_hts[5], height=_g_hts[6]),
    )
    if _bwlen==2:
        grid_chart.add(  # 加入关键词量图
            bd_bar2,
            grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top=_g_hts[7], height=_g_hts[8]),
        )
        grid_chart.add(  # 加入关键词量图
            bd_qut_line2,
            grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top=_g_hts[9], height=_g_hts[10]),
        )        
    # grid_chart.render("大量数据展示.html")
    return grid_chart


def multi_tab_echarts(notebook=False,start='2022-01-01',end='2023-08-04',**kwargs):
    IdxKey = (
        ('上证综指','股市,a股','股市Ⅰ'),
        ('上证综指','上证,上证指数','股市Ⅱ'),
        ('上证综指','牛市,熊市','牛熊'),
        ('沪深300','沪深300','沪深'),
        ('创业板指','创业板指','创业板')
    )
    tab = Tab()
    for k in IdxKey:
        tab.add(make_echarts(k[0],k[1],start,end,**kwargs),k[2])
    tab.add(make_echarts('螺纹钢','螺纹钢',beg='2021-09-01',end=end), '螺纹钢')
    tab.add(make_echarts('原油','原油',beg='2021-09-01',end=end), '原油')
    tab.add(make_echarts('生猪','生猪',beg='2021-09-01',end=end), '生猪')
    if notebook:
        return tab
    else:
        tab.render('stockPlot.html')


if __name__=='__main__':
    # get_stock_bdkey('000001',('股市','上证指数','a股'), '2021-12-20','2022-06-30')
    # get_stock_bdkey('RB0','螺纹钢', '2023-03-01','2023-08-02')
    # make_stk_plts(0)
    # make_echarts('上证综指','牛市,熊市',beg='2022-09-01',end='2023-07-28')
    # multi_tab_echarts(start='2022-08-10',end='2023-09-05')
    make_windA_echarts(beg='2005-01-01',end='2023-09-01')
    # make_marg_echarts()
    pass