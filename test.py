from common import trade_date
from data_cper import *

def update_files(retry:int=3):
    # 交易日 QVIX 分钟级数据
    for r in range(retry):
        try:
            append_qvix_minute_file()
            break
        except Exception as e:
            pass
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


update_files()