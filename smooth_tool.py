import pandas as pd
import numpy as np
import ta_cn.talib as ta # 技术分析
ta.init(mode=2, skipna=False, to_globals=True)

def super_smoother(gst,lens=20):
    a1 = np.exp(-1.414*np.pi*2/lens)
    b1 = 2*a1*np.cos(1.414*180*2/lens)
    c3 = -a1*a1
    c1 = 1-b1-c3
    filt = gst[:2]+[0 for _ in range(2,len(gst))]
    for i in range(2,len(gst)):
        filt[i] = c1/2*(gst[i]+gst[i-1])+b1*filt[i-1]+c3*filt[i-2]
    return np.array(filt)

def reflex(gst,lens=20):
    """ reflex curve """
    filt = super_smoother(gst,lens)
    slope = [0 for _ in range(len(gst))]
    sums = slope.copy()
    Ms = slope.copy()
    reflex = slope.copy()
    for i in range(20,len(gst)):
        slope[i] = (filt[i-lens]-filt[i])/lens
        sums[i] = filt[i] + (lens+1)/2*slope[i] - sum(filt[i-lens:i])/lens
        Ms[i] = 0.04*sums[i]*sums[i]+0.96*Ms[i-1]
        if Ms[i]!=0:
            reflex[i] = sums[i]/np.sqrt(Ms[i])
    return np.array(reflex)

def trendflex(gst,lens=20):
    """ trendflex curve """
    filt = super_smoother(gst,lens)
    sums = [0 for _ in range(len(gst))]
    Ms = sums.copy()
    trendflex = sums.copy()
    for i in range(20,len(gst)):
        sums[i] = filt[i]-sum(filt[i-20:i])/20
        Ms[i] = 0.04*sums[i]*sums[i]+0.96*Ms[i-1]
        if Ms[i]!=0:
            trendflex[i] = sums[i]/np.sqrt(Ms[i])
    return np.array(trendflex) 

def ema_tan(gst,short,long):
    """ ema-tan """
    return ta.EMA(gst,short)/ta.EMA(gst,long)-1