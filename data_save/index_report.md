
## 股指日报 (2023-08-01)

### 总括

#### 恐慌指数 2023-07-31

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.32	(**<font color="red">100.0</font>**,**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. 50ETF:	18.36	(**<font color="red">100.0</font>**,**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-07-30

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 11989 (79.6,40.8)
1. 股票:   	 42699 (**<font color="red">85.8</font>**,**<font color="red">88.6</font>**)
1. a股:   	 15123 (52.4,50.0)
1. 上证:   	  6329 (64.7,63.2)
1. 上证指数: 	180808 (59.9,51.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	  1066 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. 熊市:   	   263 (31.7,26.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-07-31

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 1312 (**<font color="red">100.0</font>**,76.3); 686 (**<font color="red">100.0</font>**,**<font color="red">83.4</font>**); 229 (72.3,53.7);
    - Low: 401 (**<font color="green">15.0</font>**,**<font color="green">11.9</font>**); 100 (**<font color="green">6.7</font>**,**<font color="green">3.6</font>**); 48 (**<font color="green">4.6</font>**,**<font color="green">3.2</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-08-01

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	1.65	(**<font color="red">93.1</font>**,47.3,59.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-07-30

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.32	(**<font color="red">100.0</font>**,**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. 50ETF:	18.36	(**<font color="red">100.0</font>**,**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 11989 (79.6,40.8)
1. 上证50: 	  2214 (**<font color="red">97.1</font>**,**<font color="red">96.7</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 18 (**<font color="red">85.7</font>**,**<font color="red">85.7</font>**); 9 (75.0,75.0); 3 (30.0,30.0);
    - Low: 2 (**<font color="green">7.1</font>**,**<font color="green">7.1</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.32	(**<font color="red">100.0</font>**,**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. 50ETF:	18.36	(**<font color="red">100.0</font>**,**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 11989 (79.6,40.8)
1. 沪深300:	  5034 (**<font color="red">100.0</font>**,**<font color="red">92.9</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 121 (**<font color="red">86.1</font>**,**<font color="red">86.1</font>**); 49 (**<font color="red">90.7</font>**,**<font color="red">90.7</font>**); 20 (42.6,42.6);
    - Low: 12 (**<font color="green">8.7</font>**,**<font color="green">7.8</font>**); 2 (**<font color="green">2.3</font>**,**<font color="green">1.9</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 11989 (79.6,40.8)
1. 中证500:	  3972 (**<font color="red">84.1</font>**,50.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 166 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**); 75 (**<font color="red">100.0</font>**,**<font color="red">98.7</font>**); 31 (55.4,53.4);
    - Low: 23 (**<font color="green">5.7</font>**,**<font color="green">8.3</font>**); 6 (**<font color="green">2.3</font>**,**<font color="green">3.1</font>**); 4 (**<font color="green">3.1</font>**,**<font color="green">3.4</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 11989 (79.6,40.8)
1. 创业板指: 	 11942 (37.3,37.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 11 (50.0,50.0); 3 (75.0,**<font color="green">18.8</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 10 (20.5,**<font color="green">17.9</font>**); 4 (**<font color="green">11.1</font>**,**<font color="green">8.3</font>**); 4 (**<font color="green">12.1</font>**,**<font color="green">11.8</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 11989 (79.6,40.8)
1. 科创50: 	  3089 (**<font color="red">100.0</font>**,**<font color="red">83.2</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 10 (**<font color="red">90.9</font>**,71.4); 2 (66.7,**<font color="green">16.7</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);
    - Low: 2 (**<font color="green">5.3</font>**,**<font color="green">6.9</font>**); 1 (**<font color="green">6.2</font>**,**<font color="green">4.2</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1654 (31.9,31.9)
1. 恒生指数: 	 14110 (64.1,52.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 15401 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 13287 (31.9,**<font color="green">3.9</font>**)
1. 道琼斯指数:	 12878 (34.0,**<font color="green">7.0</font>**)
1. 纳斯达克指数:	  9942 (66.6,29.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   771 (23.1,25.1)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
