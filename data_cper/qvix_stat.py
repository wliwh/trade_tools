import pandas as pd
import numpy as np
import re
import os
import sys
import configparser
sys.path.append('..')
os.chdir(os.path.dirname(__file__))

from common.trade_date import get_trade_day, get_delta_trade_day

def parse_symbol_str(symbol: str, minute: bool = False):
    ''' symbol 输出 '''
    rcp = re.compile(r'(index|cyb)?(1000|500|300|50)?(etf)?', re.IGNORECASE)
    c_pre, c_mid, _ = rcp.match(symbol).groups()
    if c_pre and c_pre.lower() == 'index' and c_mid == '1000':
        return 'index1000' if minute else 'Index1000'
    elif c_pre and symbol.lower() == 'cyb':
        return 'cyb' if minute else 'CYB'
    elif not c_pre and c_mid:
        if symbol.lower() in ('1000', '1000etf'):
            return 'index1000' if minute else 'Index1000'
        elif symbol[len(c_mid):].lower() in ('', 'etf'):
            return c_mid if minute else c_mid+'ETF'
    else:
        return None


def _test_parse():
    symbol_lst = [
        'index1000', 'Index1000', 'index', 'index10',
        'cyb', 'CYB', 'Cyb', 'cyb300', 'cyb12', '300cyb',
        '50', '300', '500', '1000', '200', '1000etf',
        '50Etf', 'cc300ETF', 'indexETF', '50k'
    ]
    for s in symbol_lst:
        print(s, parse_symbol_str(s))


def option_qvix(symbol: str = '50ETF') -> pd.DataFrame:
    """
    期权波动率指数 QVIX
    http://1.optbbs.com/s/vix.shtml?{symbol}
    [可选: 50ETF, 300ETF, 500ETF, CYB, Index1000]
    :return: 期权波动率指数 QVIX
    :rtype: pandas.DataFrame
    """
    symbol = parse_symbol_str(symbol, False)
    url = "http://1.optbbs.com/d/csv/d/k.csv"
    index_col_dict = {
        '50ETF': [0, 1, 2, 3, 4],
        '300ETF': [0, 9, 10, 11, 12],
        '500ETF': [0, 67, 68, 69, 70],
        'CYB': [0, 71, 72, 73, 74],
        'Index1000': [0, 25, 26, 27, 28]
    }
    temp_df = pd.read_csv(url).iloc[:, index_col_dict[symbol]]
    temp_df.columns = [
        "date",
        "open",
        "high",
        "low",
        "close",
    ]
    temp_df["date"] = pd.to_datetime(temp_df["date"]).dt.date
    temp_df.dropna(inplace=True)
    return temp_df


def option_min_qvix(symbol='50') -> pd.DataFrame:
    """
    期权波动率指数 QVIX - 分钟级
    http://1.optbbs.com/s/vix.shtml?{symbol}
    [可选: 50,300,500,cyb,index1000]
    :return: 期权波动率指数 QVIX
    :rtype: pandas.DataFrame
    """
    symbol = parse_symbol_str(symbol, True)
    url = f"http://1.optbbs.com/d/csv/d/vix{symbol}.csv"
    temp_df = pd.read_csv(url).iloc[:, :2]
    temp_df.columns = [
        "time",
        "qvix",
    ]
    return temp_df


def qvix_minute_pds(pref_date=''):
    ''' QVIX 分钟级数据汇总 '''
    qvix_min_pd = pd.DataFrame()
    sym_lsts = ('300ETF', '500ETF', 'CYB', '1000ETF')
    qvix_50 = option_min_qvix('50')
    qvix_min_pd.index = pd.to_datetime(pref_date + ' ' + qvix_50['time'])
    qvix_min_pd['50ETF'] = qvix_50['qvix'].values
    for sym in sym_lsts:
        qvix_min_pd[sym] = option_min_qvix(sym)['qvix'].values
    return qvix_min_pd


def append_qvix_minute_file(cfg_file=''):
    if not cfg_file:
        cfg_file = '../trade.ini'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get('Qvix_Minute', 'fpath'))
    up_date = config.get('Qvix_Minute', 'update_date')
    next_date = config.get('Qvix_Minute', 'next_update')
    now_date = get_trade_day(16).strftime('%Y-%m-%d')
    next_day = get_delta_trade_day(now_date).strftime('%Y-%m-%d')
    if not os.path.exists(fpth):
        print('qvix no.')
        config.set('Qvix_Minute', 'update_date', now_date)
        config.set('Qvix_Minute', 'next_update', next_day)
        config.write(open(fpth,'w'))
        qvix_pds = qvix_minute_pds(now_date)
        qvix_pds.to_csv(fpth, mode='w')
        return now_date
    elif up_date == now_date:
        print('qvix pass.')
        return 0
    elif next_date <= now_date:
        print('qvix update.')
        config.set('Qvix_Minute', 'update_date', now_date)
        config.set('Qvix_Minute', 'next_update', next_day)
        qvix_pds = qvix_minute_pds(now_date)
        qvix_pds.to_csv(fpth, mode='a', header=False)
        config.write(open(cfg_file,'w'))
        return now_date
    return 0

if __name__=='__main__':
    append_qvix_minute_file()
