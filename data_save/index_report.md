
## 股指日报 (2023-07-26)

### 总括

#### 恐慌指数 2023-07-25

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.66	(58.4,49.2,43.0)
1. 50ETF:	15.31	(63.6,53.4,48.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-24

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  9880 (52.0,28.7)
1. 股票:   	 42566 (**<font color="red">85.5</font>**,**<font color="red">88.3</font>**)
1. a股:   	 12661 (38.0,37.7)
1. 上证:   	  5880 (57.0,55.7)
1. 上证指数: 	164410 (35.2,30.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   425 (24.0,24.0)
1. 熊市:   	   241 (**<font color="green">14.0</font>**,**<font color="green">11.4</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-07-25

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 1101 (**<font color="red">100.0</font>**,35.6); 402 (**<font color="red">91.3</font>**,45.2); 130 (24.5,24.2);
    - Low: 127 (**<font color="green">1.1</font>**,**<font color="green">2.8</font>**); 30 (**<font color="green">0.0</font>**,**<font color="green">0.8</font>**); 10 (**<font color="green">0.0</font>**,**<font color="green">0.4</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-26

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	0.71	(**<font color="red">95.1</font>**,28.1,45.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-24

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.66	(58.4,49.2,43.0)
1. 50ETF:	15.31	(63.6,53.4,48.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9880 (52.0,28.7)
1. 上证50: 	  1474 (26.2,26.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 20 (**<font color="red">100.0</font>**,**<font color="red">95.2</font>**); 6 (50.0,50.0); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.66	(58.4,49.2,43.0)
1. 50ETF:	15.31	(63.6,53.4,48.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9880 (52.0,28.7)
1. 沪深300:	  3618 (21.7,**<font color="green">17.4</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 111 (**<font color="red">100.0</font>**,**<font color="red">92.3</font>**); 23 (42.6,42.6); 6 (**<font color="green">12.8</font>**,**<font color="green">12.8</font>**);
    - Low: 3 (**<font color="green">0.9</font>**,**<font color="green">0.8</font>**); 1 (**<font color="green">1.1</font>**,**<font color="green">0.9</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9880 (52.0,28.7)
1. 中证500:	  3147 (**<font color="green">13.8</font>**,**<font color="green">10.6</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 145 (**<font color="red">100.0</font>**,57.0); 28 (38.6,32.5); 9 (**<font color="green">15.5</font>**,**<font color="green">15.5</font>**);
    - Low: 14 (**<font color="green">1.0</font>**,**<font color="green">4.7</font>**); 5 (**<font color="green">1.5</font>**,**<font color="green">2.6</font>**); 1 (**<font color="green">0.0</font>**,**<font color="green">0.9</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9880 (52.0,28.7)
1. 创业板指: 	 11623 (31.0,31.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 12 (63.2,33.3); 2 (50.0,**<font color="green">12.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 1 (**<font color="green">0.0</font>**,**<font color="green">1.8</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9880 (52.0,28.7)
1. 科创50: 	  3079 (**<font color="red">99.6</font>**,**<font color="red">82.8</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 6 (54.5,40.0); 1 (33.3,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 2 (**<font color="green">5.3</font>**,**<font color="green">6.9</font>**); 2 (**<font color="green">12.5</font>**,**<font color="green">8.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1648 (31.6,31.6)
1. 恒生指数: 	 15232 (75.1,60.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	  9171 (48.2,50.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	  7011 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 道琼斯指数:	  6375 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 纳斯达克指数:	  5589 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   932 (61.1,62.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
