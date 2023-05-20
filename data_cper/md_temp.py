
Plain_Headers = '''
## 境内市场日报 {now_date}

### 总括

'''

Qvix_Day_Texts = '''
#### 恐慌指数波动

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 ({qvix_day_periods})
* 输出：指数-波动率指数-分位数

{qvix_day_tlst}

![]({qvix_day_300ETF_ppth})

'''

Bsearch_Pred_Texts = '''
#### 检索量波动

* 选用多个检索词刻画股市热度
* 其后附有*上证50、中证500、创业板*等检索情况
'''

High_Low_Texts = '''
#### 新高新低分位

* 新高新低数, 其所使用的周期长度 ({high_low_legu_periods})
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

{high_low_legu_tlst}

![]({high_low_legu_all_ppth})
'''

North_Flow_Texts = '''
#### 北向资金流入

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 ({north_flow_periods})
* 输出: 累计流入量-偏离度-分位数

{north_flow_tlst}

![]({north_flow_ppth})
'''

Margin_Purchase_Texts = '''
#### 融资买入分位

* 融资买入量与总成交量的比值
* 计算分位数所用的周期长度 ({margin_rate_periods})

{margin_rate_tlst}

![]({margin_rate_300_ppth})
'''

ETF_Amount_Texts = '''
#### ETF 成交量分位

* 按类别计的场内基金，它们每日成交额之比的历史分位数
* 计算分位数用的周期长度 ({etf_amount_periods})
* 输出：类型-当日成交额的比值-排序数

{etf_amount_tlst}

![]({etf_amount_plt_pth})
'''