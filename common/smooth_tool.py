import pandas as pd
import numpy as np
import akshare as ak
import datetime
import talib as ta

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

    llt_ser: pd.Series = pd.Series(index=price.index,dtype='float64')
    llt_ser[0], llt_ser[1] = price[0], price[1]

    for i, e in enumerate(price.values):
        if i > 1:
            v = (alpha - alpha**2 * 0.25) * e + (alpha ** 2 * 0.5) * price.iloc[i - 1] - (alpha - 3 * (
                alpha**2) * 0.25) * price.iloc[i - 2] + 2 * (1 - alpha) * llt_ser.iloc[i - 1] - (1 - alpha)**2 * llt_ser.iloc[i - 2]
            llt_ser.iloc[i] = v

    return llt_ser

def HMA(price: pd.Series, window: int) -> pd.Series:
    """HMA均线

    Args:
        price (pd.Series): 价格数据. index-date values
        window (int): 计算窗口

    Raises:
        ValueError: 必须为pd.Series

    Returns:
        pd.Series: index-date values
    """
    if not isinstance(price, pd.Series):

        raise ValueError('price必须为pd.Series')

    return ta.WMA(2 * ta.WMA(price, int(window * 0.5)) - ta.WMA(price, window),int(np.sqrt(window)))


def FRAMA(se, periods, clip=True):
    ''' 计算FRAMA均线 '''
    T = int(periods/2)
    df = se.copy()

    # 1.用窗口 W1 内的最高价和最低价计算 N1 = (最高价 – 最低价) / T
    N1 = (df.rolling(T).max()-df.rolling(T).min())/T

    # 2.用窗口 W2 内的最高价和最低价计算 N2 = (最高价 – 最低价) / T
    n2_df = df.shift(T)
    N2 = (n2_df.rolling(T).max()-n2_df.rolling(T).min())/T

    # 3.用窗口 T 内的最高价和最低价计算 N3 = (最高价 – 最低价) / (2T)
    N3 = (df.rolling(periods).max() -
          df.rolling(periods).min())/periods

    # 4.计算分形维数 D = [log(N1+N2) – log(N3)] / log(2)
    D = (np.log10(N1+N2)-np.log10(N3))/np.log10(2)

    # 5.计算指数移动平均的参数 alpha = exp(-4.6(D-1))
    alpha = np.exp(-4.6*(D-1))

    # 设置上线
    if clip:
        alpha = np.clip(alpha, 0.01, 0.2)

    FRAMA = []
    idx = min(np.argwhere(~np.isnan(alpha)))-1
    for row, data in enumerate(alpha):
        if row == (idx):
            FRAMA.append(df.iloc[row])
        elif row > (idx):
            FRAMA.append(data*df.iloc[row] +
                         (1-data)*FRAMA[-1])
        else:
            FRAMA.append(np.nan)

    FRAMA_se = pd.Series(FRAMA, index=df.index)

    return FRAMA_se

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


def high_low_ndays(ser:pd.Series, start_idx:int, close=False):
    ''' 某个序列中各元素一直大于或小于它前面元素的最大个数
        TODO: 加速
    '''
    if isinstance(close,float) and 0.8<=close<=1.0:
        clr = close
    elif close is False:
        clr = 1
    else:
        raise ValueError
    rkn = pd.Series(np.zeros_like(ser))
    for i,tmp in enumerate(ser.iloc[start_idx:]):
        sgn, tmpi = 0, i+start_idx
        for j in range(tmpi-1,-1,-1):
            if tmp>clr*ser.iloc[j] and sgn>=0:
                sgn = 1
            elif tmp<(2-clr)*ser.iloc[j] and sgn<=0:
                sgn = -1
            elif clr==1.0 and tmp==ser.iloc[j]:
                pass
            else:
                rkn.iloc[tmpi] = sgn*(tmpi-j) -sgn
                break
            if j==0:
                rkn.iloc[tmpi] = tmpi if sgn>=0 else -tmpi
    return rkn


def high_low_ndays2(ser:pd.Series, start_idx:int, close=False):
    ''' 某个序列中各元素一直大于或小于它前面元素的最大个数 '''
    if isinstance(close,float) and 0.8<=close<=1.0:
        clr = close
    elif close is False:
        clr = 1
    else:
        raise ValueError
    rkn = pd.Series(np.zeros_like(ser,dtype='int'))
    for i,tmp in enumerate(ser.iloc[start_idx:]):
        sgn, tmpi, j, vrkn = 0, i+start_idx, i+start_idx-1, 0
        while j>-1:
            jval = ser.iloc[j]
            vrkn = rkn.iloc[j]
            if sgn>=0 and tmp>clr*jval:
                sgn = 1; j-=(vrkn if vrkn>=0 else 0)
            elif sgn<=0 and tmp<(2-clr)*jval:
                sgn = -1; j-=(-vrkn if vrkn<0 else 0)
            elif clr==1 and tmp==jval:
                pass
            else:
                rkn.iloc[tmpi] = sgn*(tmpi-j-1)
                break
            j-=1
        if j==-1: rkn.iloc[tmpi] = tmpi if sgn>=0 else -tmpi
    return rkn



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

def min_max_dist_series(ser:pd.Series, winds:int=120, fn=None):
    ''' pd.Series 的最大最小分布 '''
    mm_dist_ser = ser.copy()
    mm_dist_ser.iloc[:winds]=np.nan
    if fn is None: fn = lambda x:x
    for i,bt in enumerate(ser.rolling(winds)):
        if len(bt) < winds:
            continue
        lmin, lmax = fn(bt.min()+0.01), fn(bt.max()+0.01)
        if lmax==lmin:
            val=0
        else:
            val = (fn(bt.iloc[-1]+0.01)-lmin)/(lmax-lmin)
        mm_dist_ser.iloc[i] = val*100
    return mm_dist_ser

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

def smart_min_max_dist_pd(pds:pd.DataFrame, windows=120, id_name=None, fn=None):
    ''' 最大最小分布：滚动窗口 '''
    mm_dist_pd = pds.copy()
    mm_dist_pd.iloc[:windows]=np.nan
    if fn is None:
        def fn(x): return x
    for i,bt in enumerate(pds.rolling(windows)):
        if len(bt) < windows:
            continue
        lmin = fn(0.8*bt.mean())
        lmax =  fn(bt.max())
        val = (fn(bt.iloc[-1])-lmin)/(lmax-lmin)
        val[val<0] = 0
        mm_dist_pd.iloc[i] = val*100
    return mm_dist_pd if id_name is None else mm_dist_pd[id_name]

def smart_min_max_dist_ser(ser:pd.Series, windows=120, fn=None):
    ''' 最大最小分布：滚动窗口 '''
    mm_dist_ser = ser.copy()
    mm_dist_ser.iloc[:windows]=np.nan
    if fn is None:
        def fn(x): return x
    for i,bt in enumerate(ser.rolling(windows)):
        if len(bt) < windows:
            continue
        lmin = fn(0.8*bt.mean())
        lmax =  fn(bt.max())
        if lmax==lmin:
            val=0
        else:
            val = (fn(bt.iloc[-1])-lmin)/(lmax-lmin)
        mm_dist_ser.iloc[i] = val*100
    return mm_dist_ser

def log_min_max_dist_pd(pds:pd.DataFrame, windows=120, id_name=None):
    ''' log 最大最小分布：滚动窗口 '''
    return min_max_dist_pd(pds, windows, id_name, np.log)

def log_min_max_dist_ser(ser:pd.Series, windows:int=120):
    ''' pd.Series 的 log 最大最小分布 '''
    return min_max_dist_series(ser,windows,np.log)
