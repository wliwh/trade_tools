import pandas as pd
import numpy as np
from collections import defaultdict
import efinance as ef
import os
import os.path as osp
import zigzag
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as dates
from common.trade_date import get_delta_trade_day
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Kline, Bar, Grid, Line, Tab

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

def calc_index_pct(pth:str, dt:str, comp_day:int=-1):
    ''' 计算分钟级涨跌以及量比 '''
    p_dt = get_delta_trade_day(dt,comp_day).strftime('%Y-%m-%d')
    p1 = pd.read_csv(pth,index_col=0)
    tmp = p1.loc[p1.index.map(lambda x:x[:10]==dt)]
    p_tmp = p1.loc[p1.index.map(lambda x:x[:10]==p_dt)]
    incs = (tmp['close']/tmp['pdclose']-1).values
    amtp = (tmp['amount'].cumsum().values)/(p_tmp['amount'].cumsum().values)
    if dt+' 14:59:00' not in tmp.index:
        incs = np.insert(incs,-1,incs[-2])
        amtp = np.insert(amtp,-1,amtp[-2])
    return incs, amtp

def arange_bms_index_min(dt:str,
                         idx_name:dict=BMS_Index_Name,
                         idx_pths:list=Kline_Min_Pth,
                         comp_day:int=-1) -> pd.DataFrame:
    ''' 大小指数的分钟图涨跌计算 '''
    bms_min_tb = pd.DataFrame([],columns=idx_name,
                              index=range(1,241))
    bms_amt_tb = pd.DataFrame([],columns=idx_name,
                              index=range(1,241))
    kline_name = [osp.basename(p) for p in idx_pths]
    for nm in idx_name:
        knth = kline_name.index(nm+'.csv') if nm+'.csv'\
            in kline_name else None
        if knth is None: continue
        kpth = idx_pths[knth]
        bms_min_tb[nm], bms_amt_tb[nm] = calc_index_pct(kpth,dt,comp_day)
    return bms_min_tb*100.0, bms_amt_tb

def get_index_pd(code:str,beg:str,end:str):
    _beg = beg.replace('-','').replace('/','')
    _end = end.replace('-','').replace('/','')
    df = ef.stock.get_quote_history(code,beg=_beg,end=_end,fqt=0)
    df.columns = ('name','code','date','o','h','l','c','amt','Volume','zf','inc','pct','hs')
    df.set_index('date',inplace=True)
    return df

def get_index_zig(idx_l,pct,beg,end):
    ''' 日频数据添加转向 '''
    df = get_index_pd(idx_l,beg,end)
    df.rename({'o':'Open','c':'Close','h':'High','l':'Low','vol':'Volume'},axis=1,inplace=True)
    df['Volume'] /= 1e8
    if not isinstance(df.index[0],str):
        df.index = [x.strftime('%Y-%m-%d') for x in df.index]
    zg_idx = zigzag.peak_valley_pivots_detailed(df.Close.values,pct/100,-pct/100,True,True)
    df['zig'] = df['Close'][zg_idx!=0]
    df['zig'] = df['zig'].interpolate(method='linear')
    return df

def find_first_zig(code:str,pct:int,beg:str,end:str):
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
    if lidx.size+hidx.size<3:
        return
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
                return find_first_zig(code,pct,beg,next_day)
            bd1_inc = (p1.iloc[bd1_dt[0]]['c'],p1.iloc[bd1_dt[1]]['c'])
    return dict(beg=p1.iloc[bd1_dt[0]].name,
                end=p1.iloc[bd1_dt[1]].name,
                days=bd1_dt[1]-bd1_dt[0],
                low=bd1_inc[0],
                high=bd1_inc[1],
                inc=bd1_inc[1]/bd1_inc[0]*100-100)

def make_comp_tb(beg:str,end:str,start:str,**kwargs):
    idx_name = kwargs.get('idx_name',BMS_Index_Name)
    zig_pct = kwargs.get('zig_pct',5)
    idx_ticks = kwargs.get('index_ticks',Index_Ticks)

    work_tb = defaultdict(list)
    work_clm_name = [str(t)+"'" for t in idx_ticks[:-1]] + ['inc','incD','Low2C','amtP'] + ['Zbeg','Zend','Zdays','Zinc']
    p_day, amt_day = arange_bms_index_min(start,**kwargs)
    # start日的时间点
    for nm in idx_name:
        for i_tick in idx_ticks:
            work_tb[nm].append(p_day.loc[i_tick,nm])
        work_tb[nm].append(p_day.loc[240,nm]-p_day.loc[1,nm])
        work_tb[nm].append(p_day.loc[240,nm]-p_day[nm].min())
        work_tb[nm].append(amt_day.loc[240,nm])
        zigs = find_first_zig(nm,zig_pct,beg,end)
        if zigs:
            work_tb[nm].extend([zigs['beg'],zigs['end'],zigs['days'],zigs['inc']])
        else:
            work_tb[nm].extend(['-','-','-','-'])
    return pd.DataFrame(work_tb,index=work_clm_name).transpose()

# print(make_comp_tb('2023-08-10','2023-09-20','2023-08-29',comp_day=-2))

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



def make_echarts_zig(code:str,beg='2018-06-01',end='2019-04-30',**kwargs):
    _plt_range_len = kwargs.get('df_range_len',100)
    _plt_width = kwargs.get('plt_width',1200)
    _plt_height = kwargs.get('plt_height',700)
    _plt_zig_pct = kwargs.get('zig_pct',4)
    _plt_zig_price = kwargs.get('zig_price','c')
    _plt_ma_days = kwargs.get('ma_args',(20,60))

    df = get_index_zig(code,_plt_zig_pct,'2016-01-01',end)
    for d in _plt_ma_days:
        df['ma'+str(d)] = df['Close'].rolling(d).mean()
    data = df.loc[beg:end,['Open','Close','Low','High']]
    volume_ser = df.loc[beg:end,'Volume']
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
            title_opts=opts.TitleOpts(subtitle="{} ~ {}. Zig is {}".format(beg, end, _plt_zig_pct)),
        )
    )
    kline_line = (
        Line()
        .add_xaxis(xaxis_data=data.index.tolist())
        # .add_yaxis(
        #     series_name="MA"+str(_plt_ma_days[0]),
        #     y_axis=df.loc[beg:end,'ma'+str(_plt_ma_days[0])],
        #     is_smooth=True,
        #     is_symbol_show=False,
        #     linestyle_opts=opts.LineStyleOpts(opacity=0.5),
        #     label_opts=opts.LabelOpts(is_show=False),
        # )
        # .add_yaxis(
        #     series_name="MA"+str(_plt_ma_days[1]),
        #     y_axis=df.loc[beg:end,'ma'+str(_plt_ma_days[1])],
        #     is_smooth=True,
        #     is_symbol_show=False,
        #     linestyle_opts=opts.LineStyleOpts(opacity=0.5),
        #     label_opts=opts.LabelOpts(is_show=False),
        # )
        .add_yaxis(
            series_name="zigzag",
            y_axis=df.loc[beg:end,'zig'],
            is_smooth=False,
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=3,opacity=0.8),
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

    bar = (
        Bar()
        .add_xaxis(xaxis_data=data.index.tolist())  # X轴数据
        .add_yaxis(
            series_name="Volume",
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
                type_="category",
                is_scale=True,
                grid_index=1,
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=False),
                split_number=20,
                min_="dataMin",
                max_="dataMax",
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=1,
                is_scale=True,
                split_number=2,
                axislabel_opts=opts.LabelOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="{}px".format(_plt_width),
            height="{}px".format(_plt_height),
            animation_opts=opts.AnimationOpts(animation=False),
        )
    )
    grid_chart.add_js_funcs("var barData = {}".format(data.values.tolist()))
    grid_chart.add(
        overlap_kline_line,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height="60%"),
    )
    grid_chart.add(
        bar,
        grid_opts=opts.GridOpts(
            pos_left="10%", pos_right="8%", pos_top="73%", height="18%"
        ),
    )

    # grid_chart.render("professional_kline_brush.html")
    return grid_chart

def make_codes_zig(idx_names=BMS_Index_Name,beg='2018-06-01',end='2019-04-30',**kwargs):
    tab = Tab()
    idx_names = ['国证A指'] + [a for a in idx_names if a!='国证A指']
    for nm in idx_names:
        tab.add(make_echarts_zig(nm,beg,end,**kwargs),nm)
    tab.render('codes_zig.html')

# plt_bms_index_min(arange_bms_index_min('2023-10-19'))
# print(find_zigs('国证2000',5,'2023-07-05','2023-07-26'))
make_codes_zig(beg='2022-10-10',end='2023-12-09',zig_pct=4)