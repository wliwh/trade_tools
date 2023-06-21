
## 股指日报 (2023-06-19)

### 总括

#### 恐慌指数 2023-06-16

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.34	(**<font color="green">0.0</font>**,22.8,22.8)
1. 50ETF:	15.36	(**<font color="green">0.0</font>**,**<font color="green">7.0</font>**,**<font color="green">16.2</font>**)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-16

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  8296 (**<font color="green">17.7</font>**,**<font color="green">17.7</font>**)
1. 股票:   	 44534 (**<font color="red">98.7</font>**,**<font color="red">98.9</font>**)
1. a股:   	  9366 (26.8,22.5)
1. 上证:   	  4498 (34.5,36.3)
1. 上证指数: 	148010 (**<font color="green">4.5</font>**,**<font color="green">16.9</font>**)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-16

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 644 (**<font color="red">82.1</font>**,20.9); 218 (38.7,22.7); 138 (26.6,33.0);
    - Low: 223 (**<font color="green">3.1</font>**,**<font color="green">6.2</font>**); 51 (**<font color="green">0.4</font>**,**<font color="green">1.7</font>**); 38 (**<font color="green">1.1</font>**,**<font color="green">2.5</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-19

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	0.62	(**<font color="red">81.2</font>**,26.4,44.1)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.34	(**<font color="green">0.0</font>**,22.8,22.8)
1. 50ETF:	15.36	(**<font color="green">0.0</font>**,**<font color="green">7.0</font>**,**<font color="green">16.2</font>**)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8296 (**<font color="green">17.7</font>**,**<font color="green">17.7</font>**)
1. 上证50: 	  1704 (51.5,51.7)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 7 (33.3,25.9); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 1 (**<font color="green">3.6</font>**,**<font color="green">3.6</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.34	(**<font color="green">0.0</font>**,22.8,22.8)
1. 50ETF:	15.36	(**<font color="green">0.0</font>**,**<font color="green">7.0</font>**,**<font color="green">16.2</font>**)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8296 (**<font color="green">17.7</font>**,**<font color="green">17.7</font>**)
1. 上证50: 	  1704 (51.5,51.7)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 63 (61.9,45.3); 15 (27.8,21.4); 13 (27.7,27.7);
    - Low: 10 (**<font color="green">3.3</font>**,**<font color="green">7.6</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8296 (**<font color="green">17.7</font>**,**<font color="green">17.7</font>**)
1. 中证500:	  3822 (55.1,52.5)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 76 (68.3,30.5); 17 (22.9,20.2); 12 (**<font color="green">19.3</font>**,20.7);
    - Low: 19 (**<font color="green">2.9</font>**,**<font color="green">5.5</font>**); 3 (**<font color="green">0.0</font>**,**<font color="green">1.5</font>**); 2 (**<font color="green">0.0</font>**,**<font color="green">1.7</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8296 (**<font color="green">17.7</font>**,**<font color="green">17.7</font>**)
1. 创业板指: 	 13503 (66.2,67.5)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 19 (**<font color="red">86.4</font>**,42.2); 2 (**<font color="green">14.3</font>**,**<font color="green">10.5</font>**); 1 (**<font color="green">7.7</font>**,**<font color="green">7.7</font>**);
    - Low: 2 (**<font color="green">1.8</font>**,**<font color="green">3.6</font>**); 1 (**<font color="green">2.1</font>**,**<font color="green">2.1</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8296 (**<font color="green">17.7</font>**,**<font color="green">17.7</font>**)
1. 科创50: 	  2831 (55.7,76.2)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 4 (28.6,**<font color="green">17.4</font>**); 1 (**<font color="green">8.3</font>**,**<font color="green">8.3</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**);
    - Low: 1 (**<font color="green">0.0</font>**,**<font color="green">3.4</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1602 (33.5,33.5)
1. 恒生指数: 	 11118 (31.8,30.7)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	  9222 (**<font color="red">86.9</font>**,70.4)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 14104 (**<font color="green">9.1</font>**,**<font color="green">10.4</font>**)
1. 道琼斯指数:	 14027 (**<font color="green">16.9</font>**,**<font color="green">12.1</font>**)
1. 纳斯达克指数:	 10447 (38.8,33.4)

![](../data_save\data_img\bday_IXIC.png)

