
## 股指日报 (2023-07-17)

### 总括

#### 恐慌指数 2023-07-17

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.39	(53.0,42.9,46.0)
1. 50ETF:	15.04	(53.2,44.0,50.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-16

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  8179 (27.8,**<font color="green">16.8</font>**)
1. 股票:   	 41501 (**<font color="red">86.3</font>**,**<font color="red">87.8</font>**)
1. a股:   	  9277 (**<font color="green">13.1</font>**,21.9)
1. 上证:   	  4619 (31.8,38.7)
1. 上证指数: 	148201 (**<font color="green">8.4</font>**,**<font color="green">17.2</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   432 (26.1,26.1)
1. 熊市:   	   253 (23.8,23.0)
1. 牛熊比:  	     1 (59.2,54.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-07-14

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 561 (47.0,**<font color="green">15.3</font>**); 209 (38.9,**<font color="green">19.2</font>**); 110 (**<font color="green">18.5</font>**,**<font color="green">18.2</font>**);
    - Low: 242 (**<font color="green">4.6</font>**,**<font color="green">6.8</font>**); 100 (**<font color="green">2.3</font>**,**<font color="green">3.6</font>**); 72 (**<font color="green">3.8</font>**,**<font color="green">5.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-17

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	0.50	(**<font color="red">82.3</font>**,24.1,42.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-16

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.39	(53.0,42.9,46.0)
1. 50ETF:	15.04	(53.2,44.0,50.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8179 (27.8,**<font color="green">16.8</font>**)
1. 上证50: 	  1485 (27.5,28.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 7 (33.3,25.9); 1 (**<font color="green">8.3</font>**,**<font color="green">5.9</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 3 (**<font color="green">10.7</font>**,**<font color="green">10.7</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 1 (**<font color="green">5.6</font>**,**<font color="green">5.6</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.39	(53.0,42.9,46.0)
1. 50ETF:	15.04	(53.2,44.0,50.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8179 (27.8,**<font color="green">16.8</font>**)
1. 沪深300:	  3990 (49.5,39.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 42 (40.2,28.7); 8 (**<font color="green">14.8</font>**,**<font color="green">11.4</font>**); 3 (**<font color="green">6.4</font>**,**<font color="green">6.4</font>**);
    - Low: 12 (**<font color="green">7.9</font>**,**<font color="green">9.2</font>**); 3 (**<font color="green">2.8</font>**,**<font color="green">2.8</font>**); 3 (**<font color="green">3.9</font>**,**<font color="green">3.9</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8179 (27.8,**<font color="green">16.8</font>**)
1. 中证500:	  3476 (34.9,26.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 54 (46.5,**<font color="green">19.4</font>**); 11 (**<font color="green">14.3</font>**,**<font color="green">12.0</font>**); 4 (**<font color="green">6.9</font>**,**<font color="green">6.9</font>**);
    - Low: 27 (**<font color="green">6.1</font>**,**<font color="green">9.8</font>**); 11 (**<font color="green">4.1</font>**,**<font color="green">5.6</font>**); 8 (**<font color="green">6.0</font>**,**<font color="green">6.8</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8179 (27.8,**<font color="green">16.8</font>**)
1. 创业板指: 	 11400 (26.4,29.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 4 (21.1,**<font color="green">8.9</font>**); 1 (**<font color="green">14.3</font>**,**<font color="green">5.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 11 (**<font color="green">18.2</font>**,**<font color="green">19.6</font>**); 7 (**<font color="green">14.6</font>**,**<font color="green">14.6</font>**); 4 (**<font color="green">11.8</font>**,**<font color="green">11.8</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8179 (27.8,**<font color="green">16.8</font>**)
1. 科创50: 	  2522 (49.0,64.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 3 (27.3,**<font color="green">13.0</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 5 (**<font color="green">14.3</font>**,**<font color="green">17.2</font>**); 2 (**<font color="green">8.3</font>**,**<font color="green">8.3</font>**); 1 (**<font color="green">4.5</font>**,**<font color="green">4.5</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1263 (**<font color="green">12.4</font>**,**<font color="green">10.0</font>**)
1. 恒生指数: 	 17232 (**<font color="red">90.8</font>**,72.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 12110 (**<font color="red">87.8</font>**,**<font color="red">88.1</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 13610 (32.6,**<font color="green">6.5</font>**)
1. 道琼斯指数:	 12877 (31.6,**<font color="green">6.1</font>**)
1. 纳斯达克指数:	  9674 (61.7,25.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>

