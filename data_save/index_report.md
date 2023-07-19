
## 股指日报 (2023-07-18)

### 总括

#### 恐慌指数 2023-07-18

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.34	(51.8,42.0,45.0)
1. 50ETF:	14.97	(48.6,40.7,47.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-17

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  9373 (46.5,25.4)
1. 股票:   	 41853 (**<font color="red">87.0</font>**,**<font color="red">88.4</font>**)
1. a股:   	 12861 (39.5,43.0)
1. 上证:   	  5914 (57.6,61.2)
1. 上证指数: 	167324 (39.8,41.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   402 (**<font color="green">17.0</font>**,**<font color="green">17.0</font>**)
1. 熊市:   	   254 (24.6,23.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-07-17

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 636 (55.7,**<font color="green">18.1</font>**); 275 (56.8,28.1); 125 (23.0,22.7);
    - Low: 401 (**<font color="green">10.0</font>**,**<font color="green">12.1</font>**); 183 (**<font color="green">5.6</font>**,**<font color="green">6.9</font>**); 133 (**<font color="green">8.5</font>**,**<font color="green">9.6</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-07-18

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	0.04	(51.4,**<font color="green">15.0</font>**,35.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-17

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.34	(51.8,42.0,45.0)
1. 50ETF:	14.97	(48.6,40.7,47.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9373 (46.5,25.4)
1. 上证50: 	  1646 (45.5,45.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 4 (**<font color="green">19.0</font>**,**<font color="green">14.8</font>**); 1 (**<font color="green">8.3</font>**,**<font color="green">5.9</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**);
    - Low: 4 (**<font color="green">14.3</font>**,**<font color="green">14.3</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	14.34	(51.8,42.0,45.0)
1. 50ETF:	14.97	(48.6,40.7,47.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9373 (46.5,25.4)
1. 沪深300:	  3830 (37.9,30.5)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 29 (26.8,**<font color="green">19.1</font>**); 6 (**<font color="green">11.1</font>**,**<font color="green">8.6</font>**); 2 (**<font color="green">4.3</font>**,**<font color="green">4.3</font>**);
    - Low: 16 (**<font color="green">11.1</font>**,**<font color="green">12.2</font>**); 6 (**<font color="green">5.7</font>**,**<font color="green">5.7</font>**); 3 (**<font color="green">3.9</font>**,**<font color="green">3.9</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9373 (46.5,25.4)
1. 中证500:	  3249 (20.6,**<font color="green">15.8</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 52 (44.6,**<font color="green">18.6</font>**); 14 (**<font color="green">18.6</font>**,**<font color="green">15.7</font>**); 8 (**<font color="green">13.8</font>**,**<font color="green">13.8</font>**);
    - Low: 57 (**<font color="green">18.4</font>**,21.7); 34 (**<font color="green">16.1</font>**,**<font color="green">17.3</font>**); 22 (**<font color="green">18.1</font>**,**<font color="green">18.8</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9373 (46.5,25.4)
1. 创业板指: 	 10378 (**<font color="green">4.4</font>**,**<font color="green">8.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 11 (57.9,24.4); 2 (28.6,**<font color="green">10.5</font>**); 1 (25.0,**<font color="green">7.7</font>**);
    - Low: 17 (29.1,30.4); 8 (**<font color="green">16.7</font>**,**<font color="green">16.7</font>**); 5 (**<font color="green">14.7</font>**,**<font color="green">14.7</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	  9373 (46.5,25.4)
1. 科创50: 	  2440 (39.8,60.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 3 (27.3,**<font color="green">13.0</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">8.3</font>**); 1 (**<font color="green">10.0</font>**,**<font color="green">10.0</font>**);
    - Low: 5 (**<font color="green">14.3</font>**,**<font color="green">17.2</font>**); 3 (**<font color="green">12.5</font>**,**<font color="green">12.5</font>**); 1 (**<font color="green">4.5</font>**,**<font color="green">4.5</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  3642 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. 恒生指数: 	  9017 (**<font color="green">0.0</font>**,**<font color="green">6.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	  3896 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	  7536 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 道琼斯指数:	  6614 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)
1. 纳斯达克指数:	  5243 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>

