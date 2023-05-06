import configparser
import os
import sys
import pandas as pd
import numpy as np
import akshare as ak
import efinance as ef
import datetime
import requests
sys.path.append('..')
os.chdir(os.path.dirname(__file__))

from common.trade_date import get_trade_day, get_delta_trade_day

def high_low_from_legu(symbol: str = "all") -> pd.DataFrame:
    """
    乐咕乐股-创新高、新低的股票数量
    https://www.legulegu.com/stockdata/high-low-statistics
    :param symbol: choice of {'all', 'sz50', 'hs300', 'zz500', 'cyb', 'cy50', 'kc50'}
    :type symbol: str
    :return: 创新高、新低的股票数量
    :rtype: pandas.DataFrame
    """
    if symbol in ('all', 'sz50', 'hs300', 'zz500', 'cyb', 'cy50', 'kc50'):
        url = f"https://www.legulegu.com/stockdata/member-ship/get-high-low-statistics/{symbol}"
    r = requests.get(url)
    data_json = r.json()
    temp_df = pd.DataFrame(data_json)
    temp_df["date"] = pd.to_datetime(temp_df["date"], unit="ms").dt.date
    del temp_df["indexCode"]
    temp_df.sort_values(['date'], inplace=True, ignore_index=True)
    return temp_df

def get_today_high_low_legu(date:str):
    hl_lst = list()
    sym_lst = ('all', 'sz50', 'hs300', 'zz500', 'cyb', 'cy50', 'kc50')
    for symbol in sym_lst:
        rs = high_low_from_legu(symbol).set_index('date')
        hl_lst.append(rs.loc[pd.to_datetime(date).date(),'high20':])
    hl_pd = pd.DataFrame(hl_lst).astype('int')
    hl_pd.insert(0,'symbol',sym_lst)
    return hl_pd


def append_high_low_legu_file(cfg_file=''):
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec = 'High_Low_Legu'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../dates_save', config.get(cfg_sec, 'fpath'))
    up_date = config.get(cfg_sec, 'update_date')
    next_date = config.get(cfg_sec, 'next_update')
    now_date = get_trade_day(17).strftime('%Y-%m-%d')
    next_day = get_delta_trade_day(now_date).strftime('%Y-%m-%d')
    if not os.path.exists(fpth):
        config.set(cfg_sec, 'update_date', now_date)
        config.set(cfg_sec, 'next_update', next_day)
        config.write(open(fpth,'w'))
        qvix_pds = get_today_high_low_legu(now_date)
        qvix_pds.to_csv(fpth, mode='w')
    elif up_date == now_date:
        pass
    elif next_date <= now_date:
        config.set(cfg_sec, 'update_date', now_date)
        config.set(cfg_sec, 'next_update', next_day)
        qvix_pds = get_today_high_low_legu(now_date)
        qvix_pds.to_csv(fpth, mode='a', header=False)
        config.write(open(cfg_file,'w'))


def _get_constituent_codes(cons_pd:pd.DataFrame, code: str, date: str):
    ''' 获取指数的成分股代码, 返回成分股调样的日期列表和对应表格 '''
    cons_pd = cons_pd[cons_pd['index_code'].apply(lambda x:x.endswith(code))]
    all_dates = cons_pd['trade_date'].drop_duplicates().to_list()
    new_dates = [a for a in all_dates if a>=date]
    bef_date = all_dates[all_dates.index(new_dates[0])-1 if new_dates else -1]
    new_dates.insert(0,bef_date)
    return new_dates,{k:cons_pd.loc[cons_pd['trade_date']==k,'code'].apply(lambda x:x[-6:]).to_list() for k in new_dates}

def _merge_const_quote(quote_hist:dict):
    ''' 合并成分股信息 '''
    close_pds,codes = list(),list()
    for c,p in quote_hist.items():
        close_p = p[['日期','收盘']]
        close_p.set_index('日期',inplace=True)
        close_pds.append(close_p)
        codes.append(c)
    close_pds = pd.concat(close_pds,axis=1)
    close_pds.columns = codes
    return close_pds

def _get_constituent_history(date:str, date_lst:list[str], codes:dict, N:int):
    ''' 获取成分股行情 '''
    Nds = datetime.timedelta(days=int(N*1.7))
    today_dt = datetime.date.today().strftime('%Y%m%d')
    # start_date = (pd.to_datetime(date)-Nds).strftime('%Y%m%d')
    # end_date = date_lst[1].replace('-','') if len(date_lst)>1 else today_dt
    # bef_date = date_lst[0]
    # bef_codes = codes[bef_date]
    # first_quote_dic = ef.stock.get_quote_history(bef_codes,beg=start_date,end=end_date,kl1=101,fqt=1)
    # bef_quote_pd = _merge_const_quote(first_quote_dic)
    # const_hist = {bef_date:bef_quote_pd}
    const_hist = list()
    for i in range(0,len(date_lst)):
        now_date = date_lst[i]
        start_date = (pd.to_datetime(now_date if i else date)-Nds).strftime('%Y%m%d')
        end_date = date_lst[i+1].replace('-','') if len(date_lst)>i+1 else today_dt
        now_codes = codes[now_date]
        quote_dic = ef.stock.get_quote_history(now_codes,beg=start_date,end=end_date,klt=101,fqt=1)
        now_quote_pd = _merge_const_quote(quote_dic)
        const_hist.append(now_quote_pd)
    return const_hist

def high_low_index_hist(cons_pd:pd.DataFrame,code:str,beg:str,Ns:tuple[int]):
    ''' 新高新低 '''
    Nmax = max(Ns)
    reconst_dates,reconst_codes = _get_constituent_codes(cons_pd,code,beg)
    const_hist = _get_constituent_history(beg,reconst_dates,reconst_codes,Nmax)
    change_const_lst = [beg]+reconst_dates[1:]
    columns_name = [hlw+'_'+str(n) for n in Nmax for hlw in ('low','high')]
    high_low_sats = pd.DataFrame({},columns=columns_name+['count'])
    for cdt,qpd in zip(change_const_lst, const_hist):
        for b in qpd.rolling(Nmax):
            if len(b)<Nmax: continue
            now_p = b.iloc[-1]
            if now_p.name < cdt: continue 
            # <号以调样当日的成分股计数; <= 则为调样的下一交易日
            high_low_sats.loc[now_p.name,'count'] = (~now_p.isnull()).sum(axis=0)
            for k in Nmax:
                if k==Nmax: cut_b = b
                else: cut_b = b.tail(k)
                l_ct = (now_p<=cut_b.min(axis=0)).sum(axis=0)
                h_ct = (now_p>=cut_b.max(axis=0)).sum(axis=0)
                high_low_sats.loc[now_p.name,'low_'+str(k)]=l_ct
                high_low_sats.loc[now_p.name,'top_'+str(k)]=h_ct
    return high_low_sats

def _high_low_index(code='000016',start='20221001',N=60):
    ## 废弃
    const = ak.index_stock_cons_csindex(symbol=code)
    const_codes = const['成分券代码'].to_list()
    start_day = datetime.datetime.strptime(start,'%Y%m%d')
    start_date = (start_day-datetime.timedelta(days=int(N*1.7))).strftime('%Y%m%d')
    code_hist = dict()
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


if __name__ == '__main__':
    append_high_low_legu_file()