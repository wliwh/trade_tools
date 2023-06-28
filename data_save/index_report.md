
## 股指日报 (2023-06-27)

### 总括

#### 恐慌指数 2023-06-27

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.50	(48.3,46.4,51.4)
1. 50ETF:	16.43	(54.5,45.9,47.5)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-26

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 13832 (68.6,49.8)
1. 股票:   	 49438 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. a股:   	 27191 (**<font color="red">100.0</font>**,**<font color="red">91.4</font>**)
1. 上证:   	  8875 (**<font color="red">100.0</font>**,**<font color="red">98.0</font>**)
1. 上证指数: 	211099 (**<font color="red">100.0</font>**,**<font color="red">88.0</font>**)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-27

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 374 (36.9,**<font color="green">10.7</font>**); 161 (25.8,**<font color="green">14.5</font>**); 100 (**<font color="green">15.5</font>**,20.9);
    - Low: 162 (**<font color="green">1.1</font>**,**<font color="green">4.1</font>**); 68 (**<font color="green">0.7</font>**,**<font color="green">2.3</font>**); 48 (**<font color="green">0.8</font>**,**<font color="green">3.2</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-27

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	0.37	(66.4,21.6,40.4)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.50	(48.3,46.4,51.4)
1. 50ETF:	16.43	(54.5,45.9,47.5)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 13832 (68.6,49.8)
1. 上证50: 	  1620 (42.7,43.0)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 1 (**<font color="green">4.8</font>**,**<font color="green">3.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 3 (**<font color="green">10.7</font>**,**<font color="green">10.7</font>**); 3 (**<font color="green">15.0</font>**,**<font color="green">15.0</font>**); 3 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.50	(48.3,46.4,51.4)
1. 50ETF:	16.43	(54.5,45.9,47.5)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 13832 (68.6,49.8)
1. 上证50: 	  1620 (42.7,43.0)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 18 (**<font color="green">15.5</font>**,**<font color="green">11.0</font>**); 5 (**<font color="green">9.3</font>**,**<font color="green">7.1</font>**); 4 (**<font color="green">8.5</font>**,**<font color="green">8.5</font>**);
    - Low: 12 (**<font color="green">4.9</font>**,**<font color="green">9.2</font>**); 9 (**<font color="green">8.5</font>**,**<font color="green">8.5</font>**); 8 (**<font color="green">10.5</font>**,**<font color="green">10.5</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 13832 (68.6,49.8)
1. 中证500:	  3836 (55.9,52.5)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 24 (**<font color="green">16.8</font>**,**<font color="green">7.8</font>**); 8 (**<font color="green">10.0</font>**,**<font color="green">8.4</font>**); 5 (**<font color="green">8.6</font>**,**<font color="green">8.6</font>**);
    - Low: 27 (**<font color="green">6.1</font>**,**<font color="green">9.8</font>**); 8 (**<font color="green">2.6</font>**,**<font color="green">4.1</font>**); 6 (**<font color="green">3.5</font>**,**<font color="green">5.1</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 13832 (68.6,49.8)
1. 创业板指: 	 14177 (77.6,78.5)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 6 (27.3,**<font color="green">13.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 11 (**<font color="green">18.2</font>**,**<font color="green">19.6</font>**); 3 (**<font color="green">6.2</font>**,**<font color="green">6.2</font>**); 3 (**<font color="green">8.8</font>**,**<font color="green">8.8</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 13832 (68.6,49.8)
1. 科创50: 	  2884 (59.3,78.1)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 3 (25.0,**<font color="green">13.0</font>**); 1 (**<font color="green">9.1</font>**,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 8 (25.0,27.6); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  2465 (**<font color="red">81.6</font>**,76.0)
1. 恒生指数: 	 15363 (**<font color="red">81.5</font>**,62.6)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	  9435 (**<font color="red">91.0</font>**,73.2)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 10000 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 道琼斯指数:	  8575 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 纳斯达克指数:	  6436 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

![](../data_save\data_img\bday_IXIC.png)

