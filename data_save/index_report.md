
## 股指日报 (2023-07-07)

### 总括

#### 恐慌指数 2023-07-07

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.03	(40.7,33.4,33.7)
1. 50ETF:	15.40	(58.2,47.6,48.9)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-07-06

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  9074 (32.2,23.3)
1. 股票:   	 42431 (**<font color="red">88.1</font>**,**<font color="red">89.3</font>**)
1. a股:   	 10589 (27.8,30.5)
1. 上证:   	  4908 (38.1,44.2)
1. 上证指数: 	158234 (22.1,30.3)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-07-06

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 498 (39.7,**<font color="green">12.9</font>**); 238 (46.7,23.1); 118 (20.9,20.6);
    - Low: 306 (**<font color="green">6.8</font>**,**<font color="green">8.9</font>**); 144 (**<font color="green">4.0</font>**,**<font color="green">5.3</font>**); 85 (**<font color="green">4.8</font>**,**<font color="green">6.0</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-07-07

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.43	(**<font color="green">18.9</font>**,**<font color="green">5.9</font>**,28.5)

![](../data_save\data_img\north_flow_bias_per.png)

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.03	(40.7,33.4,33.7)
1. 50ETF:	15.40	(58.2,47.6,48.9)

![](../data_save\data_img\qvix_day_50ETF_per.png)

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  9074 (32.2,23.3)
1. 上证50: 	  1512 (30.7,31.1)

![](../data_save\data_img\bday_SZ50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 2 (**<font color="green">9.5</font>**,**<font color="green">7.4</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 6 (21.4,21.4); 2 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**); 2 (**<font color="green">11.1</font>**,**<font color="green">11.1</font>**);

![](../data_save\data_img\hl_legu_sz50.png)

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	12.03	(40.7,33.4,33.7)
1. 50ETF:	15.40	(58.2,47.6,48.9)

![](../data_save\data_img\qvix_day_300ETF_per.png)

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  9074 (32.2,23.3)
1. 上证50: 	  1512 (30.7,31.1)

![](../data_save\data_img\bday_SZ50.png)

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 13 (**<font color="green">10.3</font>**,**<font color="green">7.4</font>**); 4 (**<font color="green">7.4</font>**,**<font color="green">5.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 25 (**<font color="green">17.6</font>**,**<font color="green">19.1</font>**); 13 (**<font color="green">12.3</font>**,**<font color="green">12.3</font>**); 10 (**<font color="green">13.2</font>**,**<font color="green">13.2</font>**);

![](../data_save\data_img\hl_legu_hs300.png)

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  9074 (32.2,23.3)
1. 中证500:	  3249 (20.6,**<font color="green">15.8</font>**)

![](../data_save\data_img\bday_ZZ500.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 27 (**<font color="green">19.8</font>**,**<font color="green">8.3</font>**); 7 (**<font color="green">8.6</font>**,**<font color="green">7.2</font>**); 4 (**<font color="green">6.9</font>**,**<font color="green">6.9</font>**);
    - Low: 50 (**<font color="green">15.6</font>**,**<font color="green">18.9</font>**); 32 (**<font color="green">15.0</font>**,**<font color="green">16.3</font>**); 18 (**<font color="green">14.7</font>**,**<font color="green">15.4</font>**);

![](../data_save\data_img\hl_legu_zz500.png)

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  9074 (32.2,23.3)
1. 创业板指: 	 10559 (**<font color="green">8.4</font>**,**<font color="green">11.9</font>**)

![](../data_save\data_img\bday_399006.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 1 (**<font color="green">5.0</font>**,**<font color="green">2.2</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 15 (25.5,26.8); 10 (20.8,20.8); 4 (**<font color="green">11.8</font>**,**<font color="green">11.8</font>**);

![](../data_save\data_img\hl_legu_cyb.png)

### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  9074 (32.2,23.3)
1. 科创50: 	  2352 (24.7,57.1)

![](../data_save\data_img\bday_KC50.png)

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 3 (25.0,**<font color="green">13.0</font>**); 2 (**<font color="green">20.0</font>**,**<font color="green">16.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 6 (**<font color="green">17.9</font>**,20.7); 3 (**<font color="green">12.5</font>**,**<font color="green">12.5</font>**); 2 (**<font color="green">9.1</font>**,**<font color="green">9.1</font>**);

![](../data_save\data_img\hl_legu_kc50.png)

### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  2302 (74.3,69.3)
1. 恒生指数: 	 17931 (**<font color="red">100.0</font>**,76.9)

![](../data_save\data_img\bday_HSI.png)

恒生科技指数:	 10201 (**<font color="red">81.8</font>**,**<font color="red">81.0</font>**)

![](../data_save\data_img\bday_HSTECH.png)


### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 15310 (48.8,**<font color="green">18.8</font>**)
1. 道琼斯指数:	 14290 (48.1,**<font color="green">16.3</font>**)
1. 纳斯达克指数:	  9498 (57.3,22.2)

![](../data_save\data_img\bday_IXIC.png)

