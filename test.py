import logging
from data_cper import *

logging.basicConfig(
    format='%(asctime)s [%(filename)s] - %(levelname)s: %(message)s',
    level=logging.INFO)

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
            res = append_margin_file('sh')
            ks = 'ready' if res==0 else 'to '+res
            logging.info("Update margin-sh {}.".format(ks))
            res = append_margin_file('sz')
            ks = 'ready' if res==0 else 'to '+res
            logging.info("Update margin-sz {}.".format(ks))
            break
        except Exception as e:
            logging.warning("Try update margin {} times. ({})".format(r+1,e))
        if r==retry-1: logging.error("Can't update margin data.")
    # 交易日新高新低-乐股数据
    for r in range(retry):
        try:
            res = append_high_low_legu_file()
            ks = 'ready' if res==0 else 'to '+res
            logging.info("Update high-log-legu {}".format(ks))
            break
        except Exception as e:
            logging.warning("Try update high-low-legu {} times. ({})".format(r+1,e))
        if r==retry-1: logging.error("Can't update high-low-legu.")
    # 当日ETF成交数据
    for r in range(retry):
        print('update etf amount.')
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