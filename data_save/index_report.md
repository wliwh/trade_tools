
## 股指日报 (2023-08-08)

### 总括

#### 恐慌指数 2023-08-03

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	16.97	(36.5,54.6,56.9)
1. 50ETF:	18.33	(37.8,47.9,54.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-08-07

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 10370 (58.8,31.7)
1. 股票:   	 29656 (49.6,60.1)
1. a股:   	 13390 (42.5,41.6)
1. 上证:   	  6031 (59.7,58.3)
1. 上证指数: 	169878 (43.7,37.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   554 (41.1,41.1)
1. 熊市:   	   294 (54.4,44.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-08-07

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 253 (**<font color="green">7.9</font>**,**<font color="green">6.5</font>**); 138 (**<font color="green">11.6</font>**,**<font color="green">9.7</font>**); 79 (**<font color="green">16.7</font>**,**<font color="green">9.0</font>**);
    - Low: 904 (40.7,28.1); 263 (22.2,**<font color="green">10.0</font>**); 164 (**<font color="green">18.5</font>**,**<font color="green">12.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-08-08

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	0.99	(66.1,51.3,49.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-08-07

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	16.97	(36.5,54.6,56.9)
1. 50ETF:	18.33	(37.8,47.9,54.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10370 (58.8,31.7)
1. 上证50: 	  1600 (39.1,40.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 3 (**<font color="green">14.3</font>**,**<font color="green">14.3</font>**); 1 (**<font color="green">11.1</font>**,**<font color="green">8.3</font>**); 1 (25.0,**<font color="green">10.0</font>**);
    - Low: 4 (**<font color="green">14.3</font>**,**<font color="green">14.3</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 1 (**<font color="green">5.6</font>**,**<font color="green">5.6</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	16.97	(36.5,54.6,56.9)
1. 50ETF:	18.33	(37.8,47.9,54.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10370 (58.8,31.7)
1. 沪深300:	  3907 (29.4,29.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 18 (**<font color="green">10.9</font>**,**<font color="green">10.9</font>**); 10 (**<font color="green">20.0</font>**,**<font color="green">18.5</font>**); 7 (33.3,**<font color="green">14.9</font>**);
    - Low: 19 (**<font color="green">14.8</font>**,**<font color="green">13.2</font>**); 6 (**<font color="green">6.9</font>**,**<font color="green">5.7</font>**); 5 (**<font color="green">6.6</font>**,**<font color="green">6.6</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10370 (58.8,31.7)
1. 中证500:	  3848 (63.5,44.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 39 (20.1,20.1); 25 (32.4,32.0); 14 (42.4,24.1);
    - Low: 61 (25.4,20.1); 30 (20.8,**<font color="green">14.9</font>**); 21 (20.4,**<font color="green">17.9</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10370 (58.8,31.7)
1. 创业板指: 	 10032 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 7 (31.8,31.8); 4 (57.1,25.0); 1 (33.3,**<font color="green">7.7</font>**);
    - Low: 16 (34.1,27.3); 10 (27.8,20.8); 8 (24.2,23.5);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10370 (58.8,31.7)
1. 科创50: 	  2526 (46.9,47.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 2 (**<font color="green">18.2</font>**,**<font color="green">14.3</font>**); 1 (33.3,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 8 (41.2,25.0); 3 (25.0,**<font color="green">12.5</font>**); 2 (**<font color="green">16.7</font>**,**<font color="green">9.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1662 (32.4,32.4)
1. 恒生指数: 	 14989 (72.8,58.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 10702 (46.6,52.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	  7440 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 道琼斯指数:	  6521 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 纳斯达克指数:	  5371 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   826 (38.6,32.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
