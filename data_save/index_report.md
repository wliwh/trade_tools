
## 股指日报 (2023-07-10)

### 总括

#### 恐慌指数 2023-07-10

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.94	(59.0,47.8,50.5)
1. 50ETF:	15.36	(54.6,45.0,46.8)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-07-09

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  7521 (**<font color="green">15.9</font>**,**<font color="green">11.5</font>**)
1. 股票:   	 42170 (**<font color="red">87.6</font>**,**<font color="red">88.9</font>**)
1. a股:   	 11314 (32.9,34.7)
1. 上证:   	  5108 (42.3,47.9)
1. 上证指数: 	158814 (23.1,31.0)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-07-10

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 531 (43.5,**<font color="green">14.2</font>**); 197 (35.6,**<font color="green">17.6</font>**); 100 (**<font color="green">15.5</font>**,**<font color="green">15.2</font>**);
    - Low: 391 (**<font color="green">9.7</font>**,**<font color="green">11.7</font>**); 135 (**<font color="green">3.7</font>**,**<font color="green">5.0</font>**); 68 (**<font color="green">3.5</font>**,**<font color="green">4.7</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-07-10

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.33	(26.8,**<font color="green">7.8</font>**,29.9)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.94	(59.0,47.8,50.5)
1. 50ETF:	15.36	(54.6,45.0,46.8)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7521 (**<font color="green">15.9</font>**,**<font color="green">11.5</font>**)
1. 上证50: 	  1487 (27.8,28.2)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 3 (**<font color="green">14.3</font>**,**<font color="green">11.1</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 5 (**<font color="green">17.9</font>**,**<font color="green">17.9</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 1 (**<font color="green">5.6</font>**,**<font color="green">5.6</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.94	(59.0,47.8,50.5)
1. 50ETF:	15.36	(54.6,45.0,46.8)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7521 (**<font color="green">15.9</font>**,**<font color="green">11.5</font>**)
1. 上证50: 	  1487 (27.8,28.2)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 25 (22.7,**<font color="green">16.2</font>**); 3 (**<font color="green">5.6</font>**,**<font color="green">4.3</font>**); 1 (**<font color="green">2.1</font>**,**<font color="green">2.1</font>**);
    - Low: 16 (**<font color="green">10.4</font>**,**<font color="green">12.2</font>**); 6 (**<font color="green">5.7</font>**,**<font color="green">5.7</font>**); 3 (**<font color="green">3.9</font>**,**<font color="green">3.9</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7521 (**<font color="green">15.9</font>**,**<font color="green">11.5</font>**)
1. 中证500:	  3181 (**<font color="green">16.1</font>**,**<font color="green">12.4</font>**)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 46 (38.6,**<font color="green">16.1</font>**); 9 (**<font color="green">11.4</font>**,**<font color="green">9.6</font>**); 4 (**<font color="green">6.9</font>**,**<font color="green">6.9</font>**);
    - Low: 36 (**<font color="green">9.8</font>**,**<font color="green">13.4</font>**); 19 (**<font color="green">8.3</font>**,**<font color="green">9.7</font>**); 10 (**<font color="green">7.8</font>**,**<font color="green">8.5</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7521 (**<font color="green">15.9</font>**,**<font color="green">11.5</font>**)
1. 创业板指: 	 10789 (**<font color="green">13.5</font>**,**<font color="green">16.8</font>**)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 7 (35.0,**<font color="green">15.6</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 13 (21.8,23.2); 8 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**); 4 (**<font color="green">11.8</font>**,**<font color="green">11.8</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  7521 (**<font color="green">15.9</font>**,**<font color="green">11.5</font>**)
1. 科创50: 	  2710 (57.6,71.7)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 4 (33.3,**<font color="green">17.4</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 6 (**<font color="green">17.9</font>**,20.7); 3 (**<font color="green">12.5</font>**,**<font color="green">12.5</font>**); 1 (**<font color="green">4.5</font>**,**<font color="green">4.5</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1843 (50.7,47.3)
1. 恒生指数: 	 15439 (78.6,61.4)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	  9855 (76.1,75.6)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 14900 (44.5,**<font color="green">15.9</font>**)
1. 道琼斯指数:	 14746 (54.1,**<font color="green">19.7</font>**)
1. 纳斯达克指数:	  9546 (58.6,23.1)

![](../data_save\data_img\bday_IXIC.png)

