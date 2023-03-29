import pandas as pd
import numpy as np
import akshare as ak

def high_low_from_legu(symbol='zz500'):
    # 调用legu网查询创新高新低股票数量，可选all,sz50,hs300,zz500
    return ak.stock_a_high_low_statistics(symbol=symbol)

