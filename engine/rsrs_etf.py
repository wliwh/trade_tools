import pandas as pd
import numpy as np
import efinance as ef
import os
import sys

sys.path.append('..')
os.chdir(os.path.dirname(__file__))
from common.smooth_tool import trendflex,LLT_MA,HMA

etf_dics = {
    'zzhl':'510880',        # 中证红利
    '399006': '159915',     # 创业板
    'IXIC': '513100',       # 纳指
    'au9999': '518880'      # 黄金
}

def rsrs_score(b:pd.Series,Nd:int=25) -> float:
    ''' 根据rsrs计算得分 '''
    slst = [0 for _ in range(len(b))]
    for i in range(Nd, len(b)):
        ys = np.log(b[i-Nd:i])
        xs = np.arange(ys.size)
        slope, intercept = np.polyfit(xs, ys, 1)
        annualized_returns = np.power(np.exp(slope), 250) - 1
        r_squared = 1 - (sum((ys - (slope * xs + intercept))**2) / ((len(ys) - 1) * np.var(ys, ddof=1)))
        score = annualized_returns * r_squared
        slst[i] =  np.sign(score)*np.log(np.abs(score)+1)
    return slst

def get_rank(etf_code:str,Nd:int=25,fun=rsrs_score)->pd.DataFrame:
    df = ef.stock.get_quote_history(etf_code,beg='20190101')
    df = df[['日期','收盘']]
    df.columns = ('date','close')
    df.set_index('date',inplace=True)
    df['score'] = fun(df.close,Nd)
    return df


def rank_dfs(etf_pool,Nd=25,fun=rsrs_score):
    nls = list()
    for n,c in etf_pool.items():
        ns = get_rank(n,Nd,fun)['score']
        ns.name = n+'_score'
        nls.append(ns)
    nls =  pd.concat(nls,axis=1)
    nls.sort_index(inplace=True)
    nls.fillna(method='ffill',inplace=True)
    return nls