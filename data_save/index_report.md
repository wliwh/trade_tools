
## 股指日报 (2023-07-05)

### 总括

#### 恐慌指数 2023-07-05

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.17	(**<font color="green">15.4</font>**,**<font color="green">12.6</font>**,**<font color="green">13.0</font>**)
1. 50ETF:	15.01	(27.6,25.6,31.1)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-07-04

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  7316 (**<font color="green">13.5</font>**,**<font color="green">9.8</font>**)
1. 股票:   	 40728 (**<font color="red">84.9</font>**,**<font color="red">86.5</font>**)
1. a股:   	 10538 (27.5,30.2)
1. 上证:   	  4769 (35.1,41.6)
1. 上证指数: 	158145 (21.9,30.2)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-07-05

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 594 (50.8,**<font color="green">16.5</font>**); 225 (43.2,21.4); 114 (**<font color="green">19.7</font>**,**<font color="green">19.4</font>**);
    - Low: 293 (**<font color="green">6.3</font>**,**<font color="green">8.5</font>**); 113 (**<font color="green">2.8</font>**,**<font color="green">4.1</font>**); 60 (**<font color="green">2.9</font>**,**<font color="green">4.1</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-07-05

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.20	(32.3,**<font color="green">10.5</font>**,32.0)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.17	(**<font color="green">15.4</font>**,**<font color="green">12.6</font>**,**<font color="green">13.0</font>**)
1. 50ETF:	15.01	(27.6,25.6,31.1)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7316 (**<font color="green">13.5</font>**,**<font color="green">9.8</font>**)
1. 上证50: 	  1548 (34.8,35.2)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 8 (38.1,29.6); 3 (25.0,**<font color="green">17.6</font>**); 3 (30.0,30.0);
    - Low: 1 (**<font color="green">3.6</font>**,**<font color="green">3.6</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.17	(**<font color="green">15.4</font>**,**<font color="green">12.6</font>**,**<font color="green">13.0</font>**)
1. 50ETF:	15.01	(27.6,25.6,31.1)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7316 (**<font color="green">13.5</font>**,**<font color="green">9.8</font>**)
1. 上证50: 	  1548 (34.8,35.2)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 25 (22.7,**<font color="green">16.2</font>**); 6 (**<font color="green">11.1</font>**,**<font color="green">8.6</font>**); 3 (**<font color="green">6.4</font>**,**<font color="green">6.4</font>**);
    - Low: 13 (**<font color="green">8.0</font>**,**<font color="green">9.9</font>**); 8 (**<font color="green">7.5</font>**,**<font color="green">7.5</font>**); 5 (**<font color="green">6.6</font>**,**<font color="green">6.6</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7316 (**<font color="green">13.5</font>**,**<font color="green">9.8</font>**)
1. 中证500:	  3764 (51.9,39.9)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 56 (48.5,20.2); 15 (**<font color="green">20.0</font>**,**<font color="green">16.9</font>**); 5 (**<font color="green">8.6</font>**,**<font color="green">8.6</font>**);
    - Low: 46 (**<font color="green">13.9</font>**,**<font color="green">17.3</font>**); 23 (**<font color="green">10.4</font>**,**<font color="green">11.7</font>**); 11 (**<font color="green">8.6</font>**,**<font color="green">9.4</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7316 (**<font color="green">13.5</font>**,**<font color="green">9.8</font>**)
1. 创业板指: 	 11712 (32.8,35.3)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 7 (35.0,**<font color="green">15.6</font>**); 3 (30.0,**<font color="green">15.8</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 12 (**<font color="green">20.0</font>**,21.4); 10 (20.8,20.8); 4 (**<font color="green">11.8</font>**,**<font color="green">11.8</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7316 (**<font color="green">13.5</font>**,**<font color="green">9.8</font>**)
1. 科创50: 	  2633 (41.9,68.7)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 5 (41.7,21.7); 2 (**<font color="green">20.0</font>**,**<font color="green">16.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 8 (25.0,27.6); 5 (20.8,20.8); 2 (**<font color="green">9.1</font>**,**<font color="green">9.1</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1376 (**<font color="green">19.8</font>**,**<font color="green">18.4</font>**)
1. 恒生指数: 	 10737 (32.6,24.0)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	 11528 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 12757 (**<font color="green">16.4</font>**,**<font color="green">0.0</font>**)
1. 道琼斯指数:	 11229 (**<font color="green">4.2</font>**,**<font color="green">0.0</font>**)
1. 纳斯达克指数:	  7064 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

![](../data_save\data_img\bday_IXIC.png)

