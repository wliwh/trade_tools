
Plain_Headers = '''
## 股指日报 ({now_date})

### 总括
'''

Qvix_Day_Texts = '''
#### 恐慌指数 {qvix_day_date}

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 ({qvix_day_periods})
* 输出：指数-波动率指数-分位数

{qvix_day_tlst}

![]({qvix_day_300ETF_ppth})

'''

Bsearch_Pred_Texts = '''
#### 检索量波动 {bsearch_day_date}

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 ({bsearch_day_periods})
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

{bsearch_day_main_tlst}

![]({bsearch_day_main_ppth})

'''

High_Low_Texts = '''
#### 新高新低分位 {high_low_legu_date}

* 20-60-120日的新高新低数, 再对该数量使用周期长度 ({high_low_legu_periods}) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

{high_low_legu_all_tlst}

![]({high_low_legu_all_ppth})
'''

North_Flow_Texts = '''
#### 北向资金流入 {north_flow_date}

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 ({north_flow_periods})
* 输出: 累计流入量-偏离度-分位数

{north_flow_tlst}

![]({north_flow_ppth})
'''

Margin_Purchase_Texts = '''
#### 融资买入水位 {margin_rate_date}

* 融资买入量与总成交量的比值
* 计算分位数所用的周期长度 ({margin_rate_periods})

{margin_rate_tlst}

![]({margin_rate_300_ppth})
'''

ETF_Amount_Texts = '''
#### ETF 成交量分位 {etf_amount_date}

* 按类别计的场内基金，它们每日成交额之比的历史分位数
* 计算分位数用的周期长度 ({etf_amount_periods})
* 输出：类型-当日成交额的比值-排序数

{etf_amount_tlst}

![]({etf_amount_plt_pth})
'''

Second_Header = '''
### 主要指数分析

包括内地宽基指数、港股指数等
'''

SZ50_Texts = '''
#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 ({qvix_day_periods})
* 输出：指数-波动率指数-分位数

{qvix_day_tlst}

![]({qvix_day_50ETF_ppth})

* 上证50搜索指数
* 计算分位数所用的周期长度 ({bsearch_day_periods})
* 输出：检索词-检索量-分位数

{bsearch_day_SZ50_tlst}

![]({bsearch_day_SZ50_ppth})

* 20-60-120日的新高新低数, 再对该数量使用周期长度 ({high_low_legu_periods}) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

{high_low_legu_sz50_tlst}

![]({high_low_legu_sz50_ppth})
'''

HS300_Texts = '''
#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 ({qvix_day_periods})
* 输出：指数-波动率指数-分位数

{qvix_day_tlst}

![]({qvix_day_300ETF_ppth})

* 沪深300搜索指数
* 计算分位数所用的周期长度 ({bsearch_day_periods})
* 输出：检索词-检索量-分位数

{bsearch_day_SZ50_tlst}

![]({bsearch_day_SZ50_ppth})

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 ({high_low_legu_periods}) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

{high_low_legu_hs300_tlst}

![]({high_low_legu_hs300_ppth})
'''

ZZ500_Texts = '''
#### 中证500

* 中证500期权波动率指数
* 计算分位数所用的周期长度 ({qvix_day_periods})
* 输出：指数-波动率指数-分位数

{qvix_day_tlst}

![]({qvix_day_50ETF_ppth})

* 中证500搜索指数
* 计算分位数所用的周期长度 ({bsearch_day_periods})
* 输出：检索词-检索量-分位数

{bsearch_day_ZZ500_tlst}

![]({bsearch_day_ZZ500_ppth})

* 20-60-120日的新高新低数, 再对该数量使用周期长度 ({high_low_legu_periods}) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

{high_low_legu_zz500_tlst}

![]({high_low_legu_zz500_ppth})
'''