import pandas as pd
import numpy as np
import akshare as ak

def high_low_from_legu(symbol='zz500'):
    # 调用legu网查询创新高新低股票数量，可选all,sz50,hs300,zz500
    return ak.stock_a_high_low_statistics(symbol=symbol)

def high_low_index(code='000016',N=60,start='20221001'):
    const = ak.index_stock_cons_csindex(symbol=code)
    const_codes = const['成分券代码'].to_list()
    start_day = datetime.datetime.strptime(start,'%Y%m%d')
    start_date = (start_day-datetime.timedelta(days=int(N*1.7))).strftime('%Y%m%d')
    code_hist = dict()
    # date_index = None
    for i,s in enumerate(const_codes):
        stk = ak.stock_zh_a_hist(s,period='daily',start_date=start_date,adjust='qfq')
        # stk = stk.tail(N+1).head(N)
        stk.set_index('日期',inplace=True)
        stk = stk[['收盘']]
        # code_hist[s] = stk['收盘'].to_list()
        code_hist[s] = stk
        # if i==0:
        #     date_index = stk['日期'].to_list()
    code_pd = pd.concat(code_hist.values(),axis=1)
    code_pd.columns = code_hist.keys()
    return code_pd
    # (code_pd.iloc[-1]>=code_pd.max(axis=0)).sum()
