
## 股指日报 (2023-06-26)

### 总括

#### 恐慌指数 2023-06-26

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	16.32	(**<font color="red">100.0</font>**,**<font color="red">80.2</font>**,**<font color="red">82.0</font>**)
1. 50ETF:	17.05	(**<font color="red">99.2</font>**,77.8,73.2)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-25

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 10385 (43.8,31.8)
1. 股票:   	 46799 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. a股:   	 14387 (74.6,50.3)
1. 上证:   	  5605 (61.8,56.3)
1. 上证指数: 	162301 (32.1,35.4)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-26

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 195 (**<font color="green">6.9</font>**,**<font color="green">4.2</font>**); 95 (**<font color="green">7.9</font>**,**<font color="green">5.8</font>**); 59 (**<font color="green">3.0</font>**,**<font color="green">9.5</font>**);
    - Low: 2068 (66.3,67.3); 1078 (41.2,42.2); 842 (62.0,63.0);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-26

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	0.55	(76.9,25.0,43.0)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	16.32	(**<font color="red">100.0</font>**,**<font color="red">80.2</font>**,**<font color="red">82.0</font>**)
1. 50ETF:	17.05	(**<font color="red">99.2</font>**,77.8,73.2)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10385 (43.8,31.8)
1. 上证50: 	  1571 (37.4,37.7)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 14 (50.0,50.0); 9 (45.0,45.0); 7 (38.9,38.9);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	16.32	(**<font color="red">100.0</font>**,**<font color="red">80.2</font>**,**<font color="red">82.0</font>**)
1. 50ETF:	17.05	(**<font color="red">99.2</font>**,77.8,73.2)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10385 (43.8,31.8)
1. 上证50: 	  1571 (37.4,37.7)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 12 (**<font color="green">9.3</font>**,**<font color="green">6.6</font>**); 4 (**<font color="green">7.4</font>**,**<font color="green">5.7</font>**); 2 (**<font color="green">4.3</font>**,**<font color="green">4.3</font>**);
    - Low: 97 (74.6,74.0); 54 (50.9,50.9); 39 (51.3,51.3);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10385 (43.8,31.8)
1. 中证500:	  3470 (34.6,38.7)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 8 (**<font color="green">1.0</font>**,**<font color="green">1.2</font>**); 2 (**<font color="green">1.4</font>**,**<font color="green">1.2</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 205 (79.1,65.5); 133 (67.4,67.9); 99 (**<font color="red">84.3</font>**,**<font color="red">84.6</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10385 (43.8,31.8)
1. 创业板指: 	 12737 (52.5,54.3)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 4 (**<font color="green">18.2</font>**,**<font color="green">8.9</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 25 (43.6,44.6); 14 (29.2,29.2); 11 (32.4,32.4);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10385 (43.8,31.8)
1. 科创50: 	  2779 (52.2,74.3)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 2 (**<font color="green">16.7</font>**,**<font color="green">8.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 9 (28.6,31.0); 3 (**<font color="green">12.5</font>**,**<font color="green">12.5</font>**); 3 (**<font color="green">13.6</font>**,**<font color="green">13.6</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1888 (53.3,49.7)
1. 恒生指数: 	 12549 (53.6,42.7)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	  8639 (75.1,60.1)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 13299 (**<font color="green">6.5</font>**,**<font color="green">4.6</font>**)
1. 道琼斯指数:	 13944 (**<font color="green">19.6</font>**,**<font color="green">12.6</font>**)
1. 纳斯达克指数:	  9817 (33.1,26.0)

![](../data_save\data_img\bday_IXIC.png)

