
## 股指日报 (2023-07-04)

### 总括

#### 恐慌指数 2023-07-04

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.32	(**<font color="green">0.0</font>**,**<font color="green">0.0</font>**,**<font color="green">0.5</font>**)
1. 50ETF:	14.73	(**<font color="green">0.0</font>**,**<font color="green">5.6</font>**,**<font color="green">15.1</font>**)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-07-03

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  7511 (**<font color="green">15.8</font>**,**<font color="green">11.4</font>**)
1. 股票:   	 41538 (**<font color="red">86.4</font>**,**<font color="red">87.9</font>**)
1. a股:   	 10947 (30.4,32.6)
1. 上证:   	  4839 (36.7,43.0)
1. 上证指数: 	155851 (**<font color="green">18.0</font>**,27.2)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-07-04

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 1020 (**<font color="red">100.0</font>**,32.5); 411 (**<font color="red">93.8</font>**,46.4); 172 (37.3,36.7);
    - Low: 132 (**<font color="green">0.9</font>**,**<font color="green">3.1</font>**); 52 (**<font color="green">0.4</font>**,**<font color="green">1.7</font>**); 26 (**<font color="green">0.3</font>**,**<font color="green">1.6</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-07-04

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.01	(43.7,**<font color="green">14.3</font>**,34.8)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.32	(**<font color="green">0.0</font>**,**<font color="green">0.0</font>**,**<font color="green">0.5</font>**)
1. 50ETF:	14.73	(**<font color="green">0.0</font>**,**<font color="green">5.6</font>**,**<font color="green">15.1</font>**)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7511 (**<font color="green">15.8</font>**,**<font color="green">11.4</font>**)
1. 上证50: 	  1687 (49.8,50.0)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 10 (47.6,37.0); 1 (**<font color="green">8.3</font>**,**<font color="green">5.9</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**);
    - Low: 2 (**<font color="green">7.1</font>**,**<font color="green">7.1</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.32	(**<font color="green">0.0</font>**,**<font color="green">0.0</font>**,**<font color="green">0.5</font>**)
1. 50ETF:	14.73	(**<font color="green">0.0</font>**,**<font color="green">5.6</font>**,**<font color="green">15.1</font>**)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7511 (**<font color="green">15.8</font>**,**<font color="green">11.4</font>**)
1. 上证50: 	  1687 (49.8,50.0)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 53 (51.5,36.8); 13 (24.1,**<font color="green">18.6</font>**); 5 (**<font color="green">10.6</font>**,**<font color="green">10.6</font>**);
    - Low: 6 (**<font color="green">2.4</font>**,**<font color="green">4.6</font>**); 4 (**<font color="green">3.8</font>**,**<font color="green">3.8</font>**); 3 (**<font color="green">3.9</font>**,**<font color="green">3.9</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7511 (**<font color="green">15.8</font>**,**<font color="green">11.4</font>**)
1. 中证500:	  3781 (52.9,50.5)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 79 (71.3,29.8); 23 (31.4,26.5); 9 (**<font color="green">15.5</font>**,**<font color="green">15.5</font>**);
    - Low: 20 (**<font color="green">3.3</font>**,**<font color="green">7.1</font>**); 9 (**<font color="green">3.1</font>**,**<font color="green">4.6</font>**); 5 (**<font color="green">3.4</font>**,**<font color="green">4.3</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7511 (**<font color="green">15.8</font>**,**<font color="green">11.4</font>**)
1. 创业板指: 	 11896 (36.4,38.8)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 13 (59.1,28.9); 2 (**<font color="green">15.4</font>**,**<font color="green">10.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 4 (**<font color="green">5.5</font>**,**<font color="green">7.1</font>**); 2 (**<font color="green">4.2</font>**,**<font color="green">4.2</font>**); 1 (**<font color="green">2.9</font>**,**<font color="green">2.9</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7511 (**<font color="green">15.8</font>**,**<font color="green">11.4</font>**)
1. 科创50: 	  2721 (48.2,72.1)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 6 (50.0,26.1); 1 (**<font color="green">9.1</font>**,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 2 (**<font color="green">3.6</font>**,**<font color="green">6.9</font>**); 1 (**<font color="green">4.2</font>**,**<font color="green">4.2</font>**); 1 (**<font color="green">4.5</font>**,**<font color="green">4.5</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1909 (54.5,50.8)
1. 恒生指数: 	 10610 (30.9,22.7)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	 10827 (**<font color="red">100.0</font>**,**<font color="red">93.7</font>**)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	  7601 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 道琼斯指数:	  6216 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 纳斯达克指数:	  5120 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

![](../data_save\data_img\bday_IXIC.png)

