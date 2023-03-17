import pandas as pd
import numpy as np
import akshare as ak
import datetime
import ta_cn.talib as ta  # 技术分析
ta.init(mode=2, skipna=False, to_globals=True)

# 交易日
def get_near_trade_date(end_trade=True)->str:
    ''' 获取最近的交易日 '''
    sh_trade_date_list = ak.tool_trade_date_hist_sina()
    today_time = datetime.datetime.now()
    near_trade_date = sh_trade_date_list[sh_trade_date_list<=today_time.date()].dropna().iloc[-1 if (today_time.hour>14 and end_trade) else -2,0]
    near_trade_date = near_trade_date.strftime('%Y-%m-%d')
    return near_trade_date

# Near_Trade_Date = get_near_trade_date()

# 一些平滑工具


def super_smoother(ser: pd.Series, lens=20):
    """ 平滑工具. 二阶低通滤波器 """
    if not isinstance(ser, pd.Series):
        raise ValueError('gst must be pd.Series.')
    gst = ser.to_list()
    a1 = np.exp(-1.414*np.pi*2/lens)
    b1 = 2*a1*np.cos(1.414*180*2/lens)
    c3 = -a1*a1
    c1 = 1-b1-c3
    filt = gst[:2]+[0 for _ in range(2, len(gst))]
    for i in range(2, len(gst)):
        filt[i] = c1/2*(gst[i]+gst[i-1])+b1*filt[i-1]+c3*filt[i-2]
    return np.array(filt)


def reflex(gst, lens=20):
    """ reflex curve """
    filt = super_smoother(gst, lens)
    slope = [0 for _ in range(len(gst))]
    sums = slope.copy()
    Ms = slope.copy()
    reflex = slope.copy()
    for i in range(20, len(gst)):
        slope[i] = (filt[i-lens]-filt[i])/lens
        sums[i] = filt[i] + (lens+1)/2*slope[i] - sum(filt[i-lens:i])/lens
        Ms[i] = 0.04*sums[i]*sums[i]+0.96*Ms[i-1]
        if Ms[i] != 0:
            reflex[i] = sums[i]/np.sqrt(Ms[i])
    return np.array(reflex)


def trendflex(gst, lens=20):
    """ trendflex curve """
    filt = super_smoother(gst, lens)
    sums = [0 for _ in range(len(gst))]
    Ms = sums.copy()
    trendflex = sums.copy()
    for i in range(20, len(gst)):
        sums[i] = filt[i]-sum(filt[i-lens:i])/lens
        Ms[i] = 0.04*sums[i]*sums[i]+0.96*Ms[i-1]
        if Ms[i] != 0:
            trendflex[i] = sums[i]/np.sqrt(Ms[i])
    return np.array(trendflex)


def ema_tan(gst: pd.Series, short: int, longd: int):
    """ 计算 ema-tan
        短期EMA与长期EMA的比值. 用于衡量上涨或下降的力度 """
    if not isinstance(gst, pd.Series):
        raise ValueError('gst must be pd.Series.')
    return ta.EMA(gst, short)/ta.EMA(gst, longd)-1


def LLT_MA(price: pd.Series, alpha: float) -> pd.Series:
    """ 计算低延迟趋势线

    Args:
        price (pd.Series): 价格数据. index-date values
        alpha (float): 窗口期的倒数.比如想要窗口期为5,则为1/5

    Raises:
        ValueError: 必须为pd.Series

    Returns:
        pd.Series: index-date values
    """
    if not isinstance(price, pd.Series):
        raise ValueError('price必须为pd.Series')

    llt_ser: pd.Series = pd.Series(index=price.index)
    llt_ser[0], llt_ser[1] = price[0], price[1]

    for i, e in enumerate(price.values):
        if i > 1:
            v = (alpha - alpha**2 * 0.25) * e + (alpha ** 2 * 0.5) * price.iloc[i - 1] - (alpha - 3 * (
                alpha**2) * 0.25) * price.iloc[i - 2] + 2 * (1 - alpha) * llt_ser.iloc[i - 1] - (1 - alpha)**2 * llt_ser.iloc[i - 2]
            llt_ser.iloc[i] = v

    return llt_ser

# 根据某个时间窗口内信号的分布进行打分的工具


def lognormal_dist_per(pds, id_name='cnt', windows=120):
    ''' LogNormal 分布
        参数设置 u->Ln[50%]; sigma->1.414*(Ln[90%]-Ln[50%]) 
        可用于 qvix 数据大小的评估 '''
    log_val_lst = [0.0 for _ in range(windows-1)]
    for bt in pds.rolling(windows):
        if len(bt) < windows:
            continue
        m50, m90 = bt[id_name].quantile(0.5), bt[id_name].quantile(0.9)
        mu = np.log(m50)
        sigma = 2*(m90-m50)
        val = 0.5*np.math.erfc((mu-np.log(bt[id_name][-1]))/sigma)
        log_val_lst.append(val*100)
    return log_val_lst


def __min_max_dist_per(pds, id_name='cnt', windows=120, fn=None):
    ''' 废弃：最大最小分布 '''
    log_val_lst = [np.nan for _ in range(windows-1)]
    if fn is None:
        def fn(x): return x
    for bt in pds.rolling(windows):
        if len(bt) < windows:
            continue
        lmin, lmax = fn(bt[id_name].min()), \
            fn(bt[id_name].max())
        val = (fn(bt[id_name][-1])-lmin)/(lmax-lmin)
        log_val_lst.append(val*100)
    return log_val_lst

def min_max_dist_pd(pds:pd.DataFrame, windows=120, id_name=None, fn=None):
    ''' 最大最小分布：滚动窗口 '''
    mm_dist_pd = pds.copy()
    mm_dist_pd.iloc[:windows]=np.nan
    if fn is None:
        def fn(x): return x
    for i,bt in enumerate(pds.rolling(windows)):
        if len(bt) < windows:
            continue
        lmin, lmax = fn(bt.min()), fn(bt.max())
        val = (fn(bt.iloc[-1])-lmin)/(lmax-lmin)
        mm_dist_pd.iloc[i] = val*100
    return mm_dist_pd if id_name is None else mm_dist_pd[id_name]

def min_max_allrange_pd(pds:pd.DataFrame, id_name=None, fn=None):
    ''' 最大最小分布：全范围
        有未来函数
    '''
    mm_dist_pd = pds.copy()
    if fn is None:
        def fn(x): return x
    lmin, lmax = fn(pds.min()), fn(pds.max())
    mm_dist_pd = (fn(pds)-lmin)/(lmax-lmin)*100
    return mm_dist_pd if id_name is None else mm_dist_pd[id_name]


def log_min_max_dist_pd(pds:pd.DataFrame, windows=120, id_name=None):
    ''' log 最大最小分布：滚动窗口 '''
    return min_max_dist_pd(pds, windows, id_name, np.log)
