
## 股指日报 (2023-06-28)

### 总括

#### 恐慌指数 2023-06-28

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.19	(28.9,33.7,39.9)
1. 50ETF:	15.69	(**<font color="green">14.3</font>**,**<font color="green">17.2</font>**,24.4)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-27

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 10979 (48.7,35.3)
1. 股票:   	 46561 (**<font color="red">95.3</font>**,**<font color="red">95.8</font>**)
1. a股:   	 16505 (61.8,59.1)
1. 上证:   	  6502 (67.5,69.8)
1. 上证指数: 	177590 (53.3,53.4)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-28

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 443 (48.4,**<font color="green">13.2</font>**); 200 (36.4,**<font color="green">19.7</font>**); 108 (**<font color="green">17.9</font>**,21.6);
    - Low: 546 (**<font color="green">14.2</font>**,**<font color="green">16.9</font>**); 202 (**<font color="green">6.1</font>**,**<font color="green">7.6</font>**); 132 (**<font color="green">7.3</font>**,**<font color="green">9.6</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-28

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	0.14	(52.7,**<font color="green">17.2</font>**,37.0)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.19	(28.9,33.7,39.9)
1. 50ETF:	15.69	(**<font color="green">14.3</font>**,**<font color="green">17.2</font>**,24.4)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10979 (48.7,35.3)
1. 上证50: 	  1522 (31.8,32.2)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 5 (23.8,**<font color="green">18.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 5 (**<font color="green">17.9</font>**,**<font color="green">17.9</font>**); 4 (**<font color="green">20.0</font>**,**<font color="green">20.0</font>**); 4 (22.2,22.2);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.19	(28.9,33.7,39.9)
1. 50ETF:	15.69	(**<font color="green">14.3</font>**,**<font color="green">17.2</font>**,24.4)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10979 (48.7,35.3)
1. 上证50: 	  1522 (31.8,32.2)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 25 (22.7,**<font color="green">16.2</font>**); 7 (**<font color="green">13.0</font>**,**<font color="green">10.0</font>**); 3 (**<font color="green">6.4</font>**,**<font color="green">6.4</font>**);
    - Low: 22 (**<font color="green">13.1</font>**,**<font color="green">16.8</font>**); 17 (**<font color="green">16.0</font>**,**<font color="green">16.0</font>**); 15 (**<font color="green">19.7</font>**,**<font color="green">19.7</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10979 (48.7,35.3)
1. 中证500:	  3918 (60.4,55.4)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 33 (25.7,**<font color="green">11.1</font>**); 10 (**<font color="green">12.9</font>**,**<font color="green">10.8</font>**); 5 (**<font color="green">8.6</font>**,**<font color="green">8.6</font>**);
    - Low: 55 (**<font color="green">17.6</font>**,20.9); 22 (**<font color="green">9.8</font>**,**<font color="green">11.2</font>**); 18 (**<font color="green">13.9</font>**,**<font color="green">15.4</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10979 (48.7,35.3)
1. 创业板指: 	 12851 (54.6,56.3)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 7 (31.8,**<font color="green">15.6</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 19 (32.7,33.9); 11 (22.9,22.9); 8 (23.5,23.5);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	 10979 (48.7,35.3)
1. 科创50: 	  2743 (49.7,72.9)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 3 (25.0,**<font color="green">13.0</font>**); 2 (**<font color="green">18.2</font>**,**<font color="green">16.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 9 (28.6,31.0); 4 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**); 3 (**<font color="green">13.6</font>**,**<font color="green">13.6</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1893 (53.6,50.0)
1. 恒生指数: 	 11996 (48.2,38.2)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	 10007 (**<font color="red">100.0</font>**,**<font color="red">82.0</font>**)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 16072 (43.2,24.6)
1. 道琼斯指数:	 15209 (47.7,22.6)
1. 纳斯达克指数:	 10515 (71.0,35.3)

![](../data_save\data_img\bday_IXIC.png)

