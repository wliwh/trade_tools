import logging
from data_cper import *

logging.basicConfig(
    format='%(asctime)s [%(filename)s] - %(levelname)s: %(message)s',
    level=logging.INFO)

def basic_append_fun(fn,retry,**kwds):
    args, wsec = kwds.get('args',[]), kwds['words']
    args = args if isinstance(args,(list,tuple)) else [args]
    for r in range(retry):
        try:
            res = fn(*args)
            ks = 'ready' if res==0 else 'to '+res
            logging.info("Update {} {}.".format(wsec, ks))
            break
        except Exception as e:
            logging.warning("Try update {} {} times. ({})".format(wsec,r+1,e))
        if r==retry-1:
            logging.error("Can't update {}.".format(wsec))

def update_files(retry:int=3):
    # 交易日 QVIX 分钟级数据
    basic_append_fun(append_qvix_minute_file,retry,words='qvix minute')
    # ;; QVIX 数据
    # bdsearch 检索词数据
    basic_append_fun(append_bsearch_day_file,retry,words='bdsearch day')
    basic_append_fun(append_bsearch_hour_file,retry,words='bdsearch hour')
    # ;; 北上资金
    # 延迟的两融数据
    basic_append_fun(append_margin_file,retry,args='sh',words='margin-sh')
    basic_append_fun(append_margin_file,retry,args='sz',words='margin-sz')
    # 交易日新高新低-乐股数据
    basic_append_fun(append_high_low_legu_file,retry,words='high-low-legu')
    # 当日ETF成交数据
    for r in range(retry):
        try:
            tm_rg, res = append_funds_trade_file()
            ks = 'ready' if res==0 else 'to '+res
            tm_rg = '' if tm_rg==0 else ' '+tm_rg
            logging.info("Update{} etf amount {}.".format(tm_rg,ks))
            break
        except Exception as e:
            logging.warning("Try update etf amount {} times. ({})".format(r+1,e))
        if r==retry-1: logging.error("Can't update etf amount.")

if __name__=='__main__':
    update_files()