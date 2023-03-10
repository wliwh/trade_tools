import numpy as np
import pandas as pd
import akshare as ak
import efinance as ef

G_base_code = '000300'      # 用于择时的指数
G_N = 18                    # rsrs 线性回归系数
G_M = 600                   # rsrs 斜率排行系数
G_K = 8                     # index 线性回归系数
G_momentum_day = 20         # 最新动量的天数
G_biasN = 90                # 乖离动量的天数
G_score_thr = -0.68
G_idex_slope_raise_thr = 12
G_score_fall_thr = -0.43
G_lossN = 20                # 止损MA20---60分钟
G_lossFactor = 1.005        # 下跌止损的比例，相对前一天的收盘价
G_SwitchFactor = 1.04       # 换仓位的比例，待换股相对当前持股的分数
G_Motion_1diff = 19         # 前一天动量变化速度门限
G_raiser_thr = 4.8          # 前一天上涨的比例门限


def get_ols(x, y):
    slope, intercept = np.polyfit(x, y, 1)
    r2 = 1 - (sum((y - (slope * x + intercept))**2) /
              ((len(y) - 1) * np.var(y, ddof=1)))
    return (intercept, slope, r2)


def get_zscore(slope_series):
    mean = np.mean(slope_series)
    std = np.std(slope_series)
    return (slope_series[-1] - mean) / std


def get_zscore_slope(z_scores):
    y = z_scores
    x = np.arange(len(z_scores))
    slope, intercept = np.polyfit(x, y, 1)
    return slope


def get_trade_signal(code=G_base_code, N=G_N, M=G_M, K=G_K):
    ''' 基于RSRS方法获取关于指数[code]的开平仓信号 '''
    base_date = ef.stock.get_quote_history(
        code, beg='20180101', klt=101, fqt=2)
    base_date = base_date[['日期', '收盘', '最低', '最高']]
    base_date.columns = ['date', 'close', 'low', 'high']
    base_date.set_index('date', inplace=True)
    intercept = [np.nan for _ in range(N-1)]
    slope = intercept.copy()
    r2 = intercept.copy()
    zscore = [np.nan for _ in range(M-1)]
    zscore_slope = [np.nan for _ in range(M+K+N-3)]
    idx_slope = [np.nan for _ in range(K-1)]
    for k in base_date.rolling(N):
        if len(k) >= N:
            a1, a2, a3 = get_ols(k['low'], k['high'])
            intercept.append(a1)
            slope.append(a2)
            r2.append(a3)
            if len(intercept) >= M:
                zscore.append(get_zscore(slope[-M:]))
    base_date['intercept'] = intercept
    base_date['slope'] = slope
    base_date['r2'] = r2
    base_date['zscore'] = zscore
    base_date['rsrs_score'] = base_date['zscore'] * base_date['r2']
    for k in base_date.rolling(K):
        if all(~k['rsrs_score'].isna()):
            zscore_slope.append(get_zscore_slope(k['rsrs_score']))
    for k in base_date.rolling(K):
        if len(k) >= K:
            idx_slope.append(get_zscore_slope(k['close']))
    base_date['rsrs_slope'] = zscore_slope
    base_date['index_slope'] = idx_slope
    base_date['buy?'] = 'sell'
    base_date.loc[(base_date['rsrs_score'] > G_score_thr), 'buy?'] = 'buy'
    base_date.loc[(base_date['index_slope'] > G_idex_slope_raise_thr) & (
        base_date['rsrs_slope'] > 0), 'buy?'] = 'buy'
    base_date.loc[(base_date['rsrs_slope'] < 0) & (
        base_date['rsrs_score'] > 0), 'buy?'] = 'sell'
    base_date.loc[(base_date['index_slope'] < 0) & (base_date['rsrs_slope'] > 0) & (
        base_date['rsrs_score'] < G_score_fall_thr), 'buy?'] = 'sell'
    return base_date


def get_bias_slope(end_date='20230306'):
    # 股票代码列表
    stock_codes = ['510300', '510050', '159949', '159928']
    momentum_days = 20
    bias_n = 90
    ans = []
    
    for code in stock_codes:
        # 获取股票收盘价数据
        quote_history = ef.stock.get_quote_history(code, beg='20220101', end=end_date, klt=101, fqt=1)
        quote_history = quote_history[['日期', '收盘']]
        quote_history.columns = ['date', 'close']
        
        # 计算乖离率
        bias_l = (quote_history.close / quote_history.close.rolling(bias_n).mean())[-momentum_days:]
        
        # 计算乖离动量拟合
        slope = np.polyfit(np.arange(momentum_days), bias_l / bias_l.iloc[0], 1)[0].real * 10000
        
        # 计算涨跌幅度
        change_rate = 100 * (quote_history.close.iloc[-1] - quote_history.close.iloc[-2]) / quote_history.close.iloc[-2]
        
        ans.append((code, slope, change_rate))
    
    return ans
