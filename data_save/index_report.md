
## 股指日报 (2023-07-20)

### 总括

#### 恐慌指数 2023-07-20

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	15.35	(**<font color="red">84.3</font>**,68.3,70.0)
1. 50ETF:	15.66	(79.0,62.6,66.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-18

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  8540 (33.7,**<font color="green">19.5</font>**)
1. 股票:   	 42472 (**<font color="red">88.1</font>**,**<font color="red">89.4</font>**)
1. a股:   	 10617 (24.0,30.6)
1. 上证:   	  5278 (45.7,50.8)
1. 上证指数: 	161173 (30.1,34.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   408 (**<font color="green">18.9</font>**,**<font color="green">18.9</font>**)
1. 熊市:   	   265 (33.3,30.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-07-20

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 375 (25.5,**<font color="green">8.3</font>**); 117 (**<font color="green">13.9</font>**,**<font color="green">6.9</font>**); 49 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 970 (29.3,30.9); 307 (**<font color="green">10.6</font>**,**<font color="green">11.8</font>**); 183 (**<font color="green">12.3</font>**,**<font color="green">13.4</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-20

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	-0.17	(38.0,**<font color="green">11.1</font>**,32.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-18

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	15.35	(**<font color="red">84.3</font>**,68.3,70.0)
1. 50ETF:	15.66	(79.0,62.6,66.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8540 (33.7,**<font color="green">19.5</font>**)
1. 上证50: 	  1482 (27.2,27.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 4 (26.7,**<font color="green">17.4</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 5 (**<font color="green">17.9</font>**,**<font color="green">17.9</font>**); 3 (**<font color="green">15.0</font>**,**<font color="green">15.0</font>**); 3 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	15.35	(**<font color="red">84.3</font>**,68.3,70.0)
1. 50ETF:	15.66	(79.0,62.6,66.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8540 (33.7,**<font color="green">19.5</font>**)
1. 沪深300:	  3731 (30.5,24.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 18 (22.4,**<font color="green">11.8</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 41 (31.0,31.3); 19 (**<font color="green">17.9</font>**,**<font color="green">17.9</font>**); 15 (**<font color="green">19.7</font>**,**<font color="green">19.7</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8540 (33.7,**<font color="green">19.5</font>**)
1. 中证500:	  3220 (**<font color="green">18.6</font>**,**<font color="green">14.4</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 41 (36.2,**<font color="green">14.0</font>**); 6 (**<font color="green">7.1</font>**,**<font color="green">6.0</font>**); 2 (**<font color="green">3.4</font>**,**<font color="green">3.4</font>**);
    - Low: 96 (34.4,37.0); 44 (21.2,22.4); 26 (21.6,22.2);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8540 (33.7,**<font color="green">19.5</font>**)
1. 创业板指: 	 10422 (**<font color="green">5.4</font>**,**<font color="green">8.9</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 1 (**<font color="green">5.3</font>**,**<font color="green">2.2</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 33 (58.2,58.9); 15 (31.2,31.2); 8 (23.5,23.5);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  8540 (33.7,**<font color="green">19.5</font>**)
1. 科创50: 	  2682 (66.2,70.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 1 (**<font color="green">9.1</font>**,**<font color="green">4.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 13 (42.9,44.8); 8 (33.3,33.3); 4 (**<font color="green">18.2</font>**,**<font color="green">18.2</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1896 (43.7,43.7)
1. 恒生指数: 	 15292 (75.6,60.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	  8801 (44.6,45.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 14141 (40.2,**<font color="green">11.0</font>**)
1. 道琼斯指数:	 13202 (36.5,**<font color="green">9.5</font>**)
1. 纳斯达克指数:	  9745 (63.2,27.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>

