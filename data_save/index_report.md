
## 股指日报 (2023-07-14)

### 总括

#### 恐慌指数 2023-07-14

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.17	(43.2,35.0,38.4)
1. 50ETF:	14.80	(40.1,34.6,42.2)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-12

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  8706 (41.6,20.7)
1. 股票:   	 42534 (**<font color="red">88.3</font>**,**<font color="red">89.5</font>**)
1. a股:   	 11606 (34.8,36.4)
1. 上证:   	  5069 (41.5,47.2)
1. 上证指数: 	155064 (20.1,26.2)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>


#### 新高新低分位 2023-07-13

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 748 (68.6,22.3); 242 (47.8,23.7); 124 (22.7,22.4);
    - Low: 131 (**<font color="green">0.8</font>**,**<font color="green">3.1</font>**); 48 (**<font color="green">0.2</font>**,**<font color="green">1.5</font>**); 29 (**<font color="green">0.5</font>**,**<font color="green">1.8</font>**);

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-14

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	0.55	(**<font color="red">85.8</font>**,25.1,43.1)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析

包括内地宽基指数、港股指数等

#### 上证50

* 上证50期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.17	(43.2,35.0,38.4)
1. 50ETF:	14.80	(40.1,34.6,42.2)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

* 上证50搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8706 (41.6,20.7)
1. 上证50: 	  1468 (25.5,26.0)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 12 (57.1,44.4); 1 (**<font color="green">8.3</font>**,**<font color="green">5.9</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**);
    - Low: 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

* 沪深300期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.17	(43.2,35.0,38.4)
1. 50ETF:	14.80	(40.1,34.6,42.2)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

* 沪深300搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8706 (41.6,20.7)
1. 沪深300:	  3741 (31.2,25.1)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

* 沪深300成分股20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 70 (69.1,49.3); 9 (**<font color="green">16.7</font>**,**<font color="green">12.9</font>**); 4 (**<font color="green">8.5</font>**,**<font color="green">8.5</font>**);
    - Low: 2 (**<font color="green">0.0</font>**,**<font color="green">1.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

* 中证500搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8706 (41.6,20.7)
1. 中证500:	  3410 (30.9,23.8)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 90 (**<font color="red">82.2</font>**,34.3); 19 (25.7,21.7); 10 (**<font color="green">17.2</font>**,**<font color="green">17.2</font>**);
    - Low: 13 (**<font color="green">0.4</font>**,**<font color="green">4.3</font>**); 6 (**<font color="green">1.6</font>**,**<font color="green">3.1</font>**); 2 (**<font color="green">0.9</font>**,**<font color="green">1.7</font>**);

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

* 创业板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8706 (41.6,20.7)
1. 创业板指: 	 11142 (21.0,24.0)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 16 (**<font color="red">84.2</font>**,35.6); 2 (28.6,**<font color="green">10.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 3 (**<font color="green">3.6</font>**,**<font color="green">5.4</font>**); 2 (**<font color="green">4.2</font>**,**<font color="green">4.2</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

* 科创板搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 股市:   	  8706 (41.6,20.7)
1. 科创50: 	  2650 (62.8,69.4)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 8 (72.7,34.8); 2 (**<font color="green">20.0</font>**,**<font color="green">16.7</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**);
    - Low: 3 (**<font color="green">7.1</font>**,**<font color="green">10.3</font>**); 2 (**<font color="green">8.3</font>**,**<font color="green">8.3</font>**); 1 (**<font color="green">4.5</font>**,**<font color="green">4.5</font>**);

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

* 恒生、恒生科技搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 港股:   	  1555 (37.9,30.5)
1. 恒生指数: 	 15538 (71.9,62.1)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 11341 (**<font color="red">97.4</font>**,**<font color="red">97.4</font>**)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

* 美股搜索指数
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数

1. 美股行情: 	 15107 (47.6,**<font color="green">17.4</font>**)
1. 道琼斯指数:	 13901 (44.0,**<font color="green">13.8</font>**)
1. 纳斯达克指数:	  9367 (54.8,21.2)

<img width="1000" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>

