
## 股指日报 (2023-08-09)

### 总括

#### 恐慌指数 2023-08-08

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.46	(31.0,50.6,53.1)
1. 50ETF:	18.78	(26.1,38.1,41.4)

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


#### 新高新低分位 2023-08-08

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 213 (**<font color="green">4.4</font>**,**<font color="green">5.1</font>**); 109 (**<font color="green">6.9</font>**,**<font color="green">6.4</font>**); 54 (**<font color="green">2.8</font>**,**<font color="green">1.5</font>**);
    - Low: 742 (32.4,22.3); 250 (21.0,**<font color="green">9.2</font>**); 156 (**<font color="green">17.5</font>**,**<font color="green">11.2</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-08-09

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	0.61	(51.4,40.1,43.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-08-07

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.46	(31.0,50.6,53.1)
1. 50ETF:	18.78	(26.1,38.1,41.4)

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
    - High: 4 (**<font color="green">19.0</font>**,**<font color="green">19.0</font>**); 2 (22.2,**<font color="green">16.7</font>**); 2 (50.0,**<font color="green">20.0</font>**);
    - Low: 3 (**<font color="green">10.7</font>**,**<font color="green">10.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.46	(31.0,50.6,53.1)
1. 50ETF:	18.78	(26.1,38.1,41.4)

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
    - High: 21 (**<font color="green">13.1</font>**,**<font color="green">13.1</font>**); 11 (22.0,20.4); 8 (38.1,**<font color="green">17.0</font>**);
    - Low: 26 (20.9,**<font color="green">18.6</font>**); 6 (**<font color="green">6.9</font>**,**<font color="green">5.7</font>**); 5 (**<font color="green">6.6</font>**,**<font color="green">6.6</font>**);

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
    - High: 31 (**<font color="green">15.1</font>**,**<font color="green">15.1</font>**); 18 (23.0,22.7); 4 (**<font color="green">12.1</font>**,**<font color="green">6.9</font>**);
    - Low: 59 (24.4,**<font color="green">19.3</font>**); 25 (**<font color="green">16.9</font>**,**<font color="green">11.9</font>**); 15 (**<font color="green">14.3</font>**,**<font color="green">12.1</font>**);

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
    - High: 3 (**<font color="green">9.5</font>**,**<font color="green">13.6</font>**); 2 (28.6,**<font color="green">12.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 16 (34.1,27.3); 13 (36.1,27.1); 9 (27.3,26.5);

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
    - High: 4 (36.4,28.6); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 10 (52.9,32.1); 5 (41.7,20.8); 5 (41.7,22.7);

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
