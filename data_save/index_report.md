
## 股指日报 (2023-07-25)

### 总括

#### 恐慌指数 2023-07-24

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.89	(69.1,47.2,50.0)
1. 50ETF:	14.84	(36.1,29.1,34.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-23

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


#### 新高新低分位 2023-07-24

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 481 (37.2,**<font color="green">12.3</font>**); 157 (24.7,**<font color="green">12.2</font>**); 53 (**<font color="green">1.2</font>**,**<font color="green">1.2</font>**);
    - Low: 761 (22.2,23.8); 208 (**<font color="green">6.6</font>**,**<font color="green">7.9</font>**); 153 (**<font color="green">10.0</font>**,**<font color="green">11.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-25

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	-0.12	(43.5,**<font color="green">12.1</font>**,33.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-23

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.89	(69.1,47.2,50.0)
1. 50ETF:	14.84	(36.1,29.1,34.8)

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
    - High: 1 (**<font color="green">6.7</font>**,**<font color="green">4.8</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 9 (32.1,32.1); 3 (**<font color="green">15.0</font>**,**<font color="green">15.0</font>**); 3 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.89	(69.1,47.2,50.0)
1. 50ETF:	14.84	(36.1,29.1,34.8)

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
    - High: 16 (**<font color="green">19.4</font>**,**<font color="green">11.1</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 50 (38.1,37.2); 20 (**<font color="green">18.9</font>**,**<font color="green">18.9</font>**); 16 (21.1,21.1);

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
    - High: 53 (48.9,**<font color="green">19.0</font>**); 6 (**<font color="green">7.1</font>**,**<font color="green">6.0</font>**); 2 (**<font color="green">3.4</font>**,**<font color="green">3.4</font>**);
    - Low: 63 (20.9,24.0); 30 (**<font color="green">14.0</font>**,**<font color="green">15.3</font>**); 23 (**<font color="green">19.0</font>**,**<font color="green">19.7</font>**);

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
    - High: 5 (26.3,**<font color="green">12.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 30 (52.7,53.6); 14 (29.2,29.2); 11 (32.4,32.4);

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
    - High: 3 (27.3,**<font color="green">20.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 18 (63.0,62.1); 10 (41.7,41.7); 4 (**<font color="green">18.2</font>**,**<font color="green">18.2</font>**);

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
