
## 股指日报 (2023-06-12)

### 总括

#### 恐慌指数 2023-06-12

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.35	(**<font color="green">8.4</font>**,31.1,31.1)
1. 50ETF:	16.47	(**<font color="green">14.4</font>**,**<font color="green">18.1</font>**,25.1)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-09

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  8592 (**<font color="green">19.9</font>**,**<font color="green">19.9</font>**)
1. 股票:   	 33087 (**<font color="red">99.2</font>**,**<font color="red">99.3</font>**)
1. a股:   	 10811 (42.2,31.8)
1. 上证:   	  4780 (38.0,41.8)
1. 上证指数: 	157113 (20.1,28.9)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-12

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 529 (62.8,**<font color="green">16.7</font>**); 185 (30.3,**<font color="green">18.4</font>**); 110 (**<font color="green">18.2</font>**,25.3);
    - Low: 419 (**<font color="green">9.9</font>**,**<font color="green">12.7</font>**); 216 (**<font color="green">7.0</font>**,**<font color="green">8.2</font>**); 168 (**<font color="green">11.1</font>**,**<font color="green">12.3</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-12

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.18	(33.5,**<font color="green">10.9</font>**,32.3)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.35	(**<font color="green">8.4</font>**,31.1,31.1)
1. 50ETF:	16.47	(**<font color="green">14.4</font>**,**<font color="green">18.1</font>**,25.1)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8592 (**<font color="green">19.9</font>**,**<font color="green">19.9</font>**)
1. 上证50: 	  2119 (**<font color="red">89.5</font>**,**<font color="red">89.2</font>**)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 2 (**<font color="green">9.5</font>**,**<font color="green">7.4</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 3 (**<font color="green">10.7</font>**,**<font color="green">10.7</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 1 (**<font color="green">5.6</font>**,**<font color="green">5.6</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.35	(**<font color="green">8.4</font>**,31.1,31.1)
1. 50ETF:	16.47	(**<font color="green">14.4</font>**,**<font color="green">18.1</font>**,25.1)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8592 (**<font color="green">19.9</font>**,**<font color="green">19.9</font>**)
1. 上证50: 	  2119 (**<font color="red">89.5</font>**,**<font color="red">89.2</font>**)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 24 (21.6,**<font color="green">17.3</font>**); 7 (**<font color="green">13.0</font>**,**<font color="green">10.0</font>**); 2 (**<font color="green">4.3</font>**,**<font color="green">4.3</font>**);
    - Low: 32 (**<font color="green">20.0</font>**,24.4); 16 (**<font color="green">13.5</font>**,**<font color="green">15.1</font>**); 11 (**<font color="green">13.3</font>**,**<font color="green">14.5</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8592 (**<font color="green">19.9</font>**,**<font color="green">19.9</font>**)
1. 中证500:	  3488 (35.7,41.6)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 53 (45.5,21.3); 14 (**<font color="green">18.6</font>**,**<font color="green">16.7</font>**); 11 (**<font color="green">17.5</font>**,**<font color="green">19.0</font>**);
    - Low: 52 (**<font color="green">16.4</font>**,**<font color="green">16.1</font>**); 31 (**<font color="green">13.2</font>**,**<font color="green">15.8</font>**); 22 (**<font color="green">14.4</font>**,**<font color="green">18.8</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8592 (**<font color="green">19.9</font>**,**<font color="green">19.9</font>**)
1. 创业板指: 	 13307 (62.8,64.2)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 8 (36.4,**<font color="green">17.8</font>**); 1 (**<font color="green">7.1</font>**,**<font color="green">5.3</font>**); 1 (**<font color="green">7.7</font>**,**<font color="green">7.7</font>**);
    - Low: 9 (**<font color="green">14.5</font>**,**<font color="green">16.1</font>**); 6 (**<font color="green">12.5</font>**,**<font color="green">12.5</font>**); 6 (**<font color="green">17.6</font>**,**<font color="green">17.6</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8592 (**<font color="green">19.9</font>**,**<font color="green">19.9</font>**)
1. 科创50: 	  3012 (69.9,**<font color="red">82.6</font>**)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 4 (28.6,**<font color="green">17.4</font>**); 2 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**); 2 (**<font color="green">20.0</font>**,**<font color="green">20.0</font>**);
    - Low: 6 (**<font color="green">17.9</font>**,20.7); 5 (20.8,20.8); 3 (**<font color="green">13.6</font>**,**<font color="green">13.6</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1396 (**<font color="green">19.8</font>**,**<font color="green">19.8</font>**)
1. 恒生指数: 	 10529 (22.0,25.4)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	  7152 (41.0,33.8)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 12934 (**<font color="green">0.0</font>**,**<font color="green">1.5</font>**)
1. 道琼斯指数:	 12912 (**<font color="green">0.2</font>**,**<font color="green">2.8</font>**)
1. 纳斯达克指数:	  9153 (**<font color="green">17.7</font>**,**<font color="green">15.9</font>**)

![](../data_save\data_img\bday_IXIC.png)

