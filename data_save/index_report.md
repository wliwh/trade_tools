
## 股指日报 (2023-08-15)

### 总括

#### 恐慌指数 2023-08-14

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	18.00	(**<font color="green">12.6</font>**,37.5,40.7)
1. 50ETF:	18.73	(**<font color="green">0.0</font>**,**<font color="green">8.4</font>**,**<font color="green">12.5</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-08-13

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 15040 (**<font color="red">100.0</font>**,55.0)
1. 股票:   	 33080 (58.2,68.6)
1. a股:   	 26654 (**<font color="red">98.4</font>**,**<font color="red">98.5</font>**)
1. 上证:   	  8909 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. 上证指数: 	205991 (**<font color="red">93.7</font>**,**<font color="red">93.5</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   516 (34.7,34.7)
1. 熊市:   	   323 (73.5,73.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-08-14

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 175 (**<font color="green">3.8</font>**,**<font color="green">3.8</font>**); 80 (**<font color="green">2.6</font>**,**<font color="green">2.6</font>**); 24 (**<font color="green">2.4</font>**,**<font color="green">1.4</font>**);
    - Low: 949 (43.0,28.6); 382 (33.6,**<font color="green">14.1</font>**); 237 (27.3,**<font color="green">17.3</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-08-15

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	-0.39	(**<font color="green">13.1</font>**,**<font color="green">13.1</font>**,29.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-08-13

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	18.00	(**<font color="green">12.6</font>**,37.5,40.7)
1. 50ETF:	18.73	(**<font color="green">0.0</font>**,**<font color="green">8.4</font>**,**<font color="green">12.5</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 15040 (**<font color="red">100.0</font>**,55.0)
1. 上证50: 	  1563 (35.0,36.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 1 (**<font color="green">4.8</font>**,**<font color="green">4.8</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 10 (35.7,35.7); 2 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**); 2 (**<font color="green">11.1</font>**,**<font color="green">11.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	18.00	(**<font color="green">12.6</font>**,37.5,40.7)
1. 50ETF:	18.73	(**<font color="green">0.0</font>**,**<font color="green">8.4</font>**,**<font color="green">12.5</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 15040 (**<font color="red">100.0</font>**,55.0)
1. 沪深300:	  4171 (42.0,42.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 4 (**<font color="green">2.2</font>**,**<font color="green">2.2</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 59 (49.6,44.2); 20 (23.0,**<font color="green">18.9</font>**); 17 (22.4,22.4);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 15040 (**<font color="red">100.0</font>**,55.0)
1. 中证500:	  3713 (54.9,38.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 8 (**<font color="green">1.9</font>**,**<font color="green">1.9</font>**); 3 (**<font color="green">2.7</font>**,**<font color="green">2.7</font>**); 1 (**<font color="green">3.0</font>**,**<font color="green">1.7</font>**);
    - Low: 108 (49.7,39.3); 50 (36.2,24.7); 40 (39.8,33.6);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 15040 (**<font color="red">100.0</font>**,55.0)
1. 创业板指: 	 10961 (20.1,20.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 1 (**<font color="green">4.5</font>**,**<font color="green">4.5</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 30 (65.9,52.7); 20 (55.6,41.7); 15 (45.5,44.1);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 15040 (**<font color="red">100.0</font>**,55.0)
1. 科创50: 	  2694 (63.9,57.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 2 (**<font color="green">18.2</font>**,**<font color="green">14.3</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 20 (**<font color="red">100.0</font>**,67.9); 10 (**<font color="red">83.3</font>**,41.7); 7 (58.3,31.8);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1622 (30.3,30.3)
1. 恒生指数: 	 15540 (77.9,62.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 10810 (45.8,52.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 13960 (53.4,**<font color="green">10.5</font>**)
1. 道琼斯指数:	 13830 (54.7,**<font color="green">16.1</font>**)
1. 纳斯达克指数:	 10198 (70.8,34.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   771 (23.1,**<font color="green">19.3</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
