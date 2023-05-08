import logging
from data_cper import *

logging.basicConfig(
    format='%(asctime)s [%(filename)s] - %(levelname)s: %(message)s',
    level=logging.DEBUG)

def update_files(retry:int=3):
    # 交易日 QVIX 分钟级数据
    for r in range(retry):
        try:
            res = append_qvix_minute_file()
            ks = 'ready' if res==0 else 'to '+res
            logging.info("Update qvix minute {}.".format(ks))
            break
        except Exception as e:
            logging.warning("Try update qvix minute {} times. ({})".format(r+1,e))
        if r==retry-1: logging.error("Can't update qvix minute.")
    # ;; QVIX 数据
    # ;; 北上资金
    # 延迟的两融数据
    for r in range(retry):
        try:
            append_margin_file('sh')
            append_margin_file('sz')
            break
        except Exception as e:
            pass
    # 交易日新高新低-乐股数据
    for r in range(retry):
        try:
            append_high_low_legu_file()
            break
        except Exception as e:
            pass
    # 当日ETF成交数据
    for r in range(retry):
        print('update etf amount.')
        try:
            append_funds_trade_file()
            break
        except Exception as e:
            pass


update_files()