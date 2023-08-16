import numpy as np
import pandas as pd
import efinance as ef
import akshare as ak
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as dates

# 从机构重仓股的滚动年化收益推断顶底

def get_funds_kline(cname:str,Ytd:int=242,Ypair=(3,)):
    e1 = ef.stock.get_quote_history(cname)
    e1 = e1[['日期','收盘']]
    e1.columns = ('date','close')
    e1 = e1.tail(Ytd*15)
    e1.set_index('date',inplace=True)
    for y in Ypair:
        yname = str(y)+'_return'
        e1[yname] = 100*(np.power(1+e1.close.pct_change(Ytd*y),1/y)-1)
    plt.figure(figsize=(8,6))
    for y in Ypair:
        plt.plot(e1.index,e1[str(y)+'_return'])
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    # ax.xaxis.set_major_formatter(lambda x:x[2:])
    plt.xticks(rotation=60)
    plt.show()

# 社融底

def get_afre_with_month():
    kls = ef.stock.get_quote_history('中证流通',klt=103)
    kls = kls.loc[:,'日期':'最低']
    kls['日期'] = kls['日期'].apply(lambda x: x[:4]+x[5:7])
    kls.set_index('日期',inplace=True)
    kls.index.name = '月份'
    kls = kls.loc['201501':]
    base_afre = 1230242 # 2014年底社融规模
    afre_amt = ak.macro_china_shrzgm().iloc[:,:2]
    afre_amt['社融存量'] = afre_amt.iloc[:,1].cumsum() + base_afre
    afre_amt.rename(columns={'社会融资规模增量':'社融增量'},inplace=True)
    afre_amt.set_index('月份',inplace=True)
    kls = kls.join(afre_amt)
    _plow, _afrec = kls.loc['201810',['最低','社融存量']]
    kls['社融存量Adj'] = kls['社融存量'] / _afrec * _plow

    fig, ax = plt.subplots()
    ax.plot(kls.index,kls['最低'],kls.index,kls['收盘'])
    ax.plot(kls.index,kls['社融存量Adj'])
    ax.set_xlabel('Month')
    ax.set_ylabel('Index')
    ax.spines['right'].set_visible(False) # ax右轴隐藏

    # z_ax = ax.twinx() # 创建与轴群ax共享x轴的轴群z_ax
    # z_ax.plot(kls.index,kls['社融存量'],'black')
    # z_ax.set_ylabel('社融规模')
    plt.show()

# get_afre_with_month()
