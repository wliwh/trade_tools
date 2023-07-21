import numpy as np
import pandas as pd
import efinance as ef
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