
## 股指日报 (2023-07-21)

### 总括

#### 恐慌指数 2023-07-21

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.66	(54.5,44.1,47.1)
1. 50ETF:	15.14	(47.6,39.9,46.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-21

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 10390 (59.2,31.8)
1. 股票:   	 44174 (**<font color="red">89.1</font>**,**<font color="red">92.0</font>**)
1. a股:   	 14768 (50.5,52.0)
1. 上证:   	  6360 (65.2,67.8)
1. 上证指数: 	169180 (42.7,43.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   399 (**<font color="green">16.1</font>**,**<font color="green">16.1</font>**)
1. 熊市:   	   268 (35.5,31.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-07-21

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 573 (48.4,**<font color="green">15.7</font>**); 182 (31.5,**<font color="green">15.6</font>**); 50 (**<font color="green">0.3</font>**,**<font color="green">0.3</font>**);
    - Low: 989 (30.0,31.6); 238 (**<font color="green">7.8</font>**,**<font color="green">9.0</font>**); 144 (**<font color="green">9.3</font>**,**<font color="green">10.5</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-21

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	0.13	(60.6,**<font color="green">16.8</font>**,36.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-21

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.66	(54.5,44.1,47.1)
1. 50ETF:	15.14	(47.6,39.9,46.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10390 (59.2,31.8)
1. 上证50: 	  1480 (27.0,27.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 4 (26.7,**<font color="green">17.4</font>**); 2 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 6 (21.4,21.4); 2 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**); 2 (**<font color="green">11.1</font>**,**<font color="green">11.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.66	(54.5,44.1,47.1)
1. 50ETF:	15.14	(47.6,39.9,46.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10390 (59.2,31.8)
1. 沪深300:	  3863 (40.3,32.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 27 (35.8,**<font color="green">18.9</font>**); 5 (**<font color="green">9.3</font>**,**<font color="green">9.1</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 45 (34.1,34.4); 19 (**<font color="green">17.9</font>**,**<font color="green">17.9</font>**); 13 (**<font color="green">17.1</font>**,**<font color="green">17.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10390 (59.2,31.8)
1. 中证500:	  3199 (**<font color="green">17.3</font>**,**<font color="green">13.3</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 70 (67.0,26.0); 10 (**<font color="green">12.9</font>**,**<font color="green">10.8</font>**); 4 (**<font color="green">6.9</font>**,**<font color="green">6.9</font>**);
    - Low: 72 (24.6,27.6); 23 (**<font color="green">10.4</font>**,**<font color="green">11.7</font>**); 14 (**<font color="green">11.2</font>**,**<font color="green">12.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10390 (59.2,31.8)
1. 创业板指: 	 11447 (27.4,30.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 9 (47.4,**<font color="green">20.0</font>**); 3 (75.0,**<font color="green">16.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 29 (50.9,51.8); 11 (22.9,22.9); 6 (**<font color="green">17.6</font>**,**<font color="green">17.6</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 10390 (59.2,31.8)
1. 科创50: 	  2985 (**<font color="red">91.3</font>**,**<font color="red">81.6</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 2 (**<font color="green">18.2</font>**,**<font color="green">8.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 13 (42.9,44.8); 7 (29.2,29.2); 3 (**<font color="green">13.6</font>**,**<font color="green">13.6</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1333 (**<font color="green">13.3</font>**,**<font color="green">13.3</font>**)
1. 恒生指数: 	 14044 (63.4,51.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	  9619 (55.3,56.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 13054 (27.3,**<font color="green">2.0</font>**)
1. 道琼斯指数:	 13329 (38.8,**<font color="green">10.0</font>**)
1. 纳斯达克指数:	 10536 (78.4,36.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   893 (52.2,67.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
