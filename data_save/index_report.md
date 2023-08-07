
## 股指日报 (2023-08-04)

### 总括

#### 恐慌指数 2023-08-04

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.26	(35.2,53.6,56.0)
1. 50ETF:	18.55	(34.3,44.9,52.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-08-04

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 13205 (**<font color="red">93.4</font>**,46.9)
1. 股票:   	 31628 (56.6,65.1)
1. a股:   	 17767 (65.5,61.2)
1. 上证:   	  6572 (68.6,67.1)
1. 上证指数: 	182231 (61.9,53.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   805 (74.7,74.7)
1. 熊市:   	   284 (47.3,38.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-08-04

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 406 (21.2,**<font color="green">16.6</font>**); 213 (23.7,**<font color="green">19.8</font>**); 115 (36.7,**<font color="green">19.7</font>**);
    - Low: 468 (**<font color="green">18.5</font>**,**<font color="green">13.5</font>**); 92 (**<font color="green">5.9</font>**,**<font color="green">3.3</font>**); 51 (**<font color="green">4.9</font>**,**<font color="green">3.5</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-08-04

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	1.34	(79.6,55.0,54.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-08-04

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.26	(35.2,53.6,56.0)
1. 50ETF:	18.55	(34.3,44.9,52.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13205 (**<font color="red">93.4</font>**,46.9)
1. 上证50: 	  1997 (78.7,78.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 7 (33.3,33.3); 2 (22.2,**<font color="green">16.7</font>**); 1 (25.0,**<font color="green">10.0</font>**);
    - Low: 1 (**<font color="green">3.6</font>**,**<font color="green">3.6</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	17.26	(35.2,53.6,56.0)
1. 50ETF:	18.55	(34.3,44.9,52.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13205 (**<font color="red">93.4</font>**,46.9)
1. 沪深300:	  4995 (76.7,76.7)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 56 (38.7,38.7); 29 (58.0,53.7); 16 (76.2,34.0);
    - Low: 8 (**<font color="green">5.2</font>**,**<font color="green">4.7</font>**); 2 (**<font color="green">2.3</font>**,**<font color="green">1.9</font>**); 1 (**<font color="green">1.3</font>**,**<font color="green">1.3</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13205 (**<font color="red">93.4</font>**,46.9)
1. 中证500:	  4484 (**<font color="red">100.0</font>**,70.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 85 (49.1,49.1); 53 (70.3,69.3); 30 (**<font color="red">90.9</font>**,51.7);
    - Low: 25 (**<font color="green">6.7</font>**,**<font color="green">5.3</font>**); 9 (**<font color="green">4.6</font>**,**<font color="green">4.1</font>**); 6 (**<font color="green">5.1</font>**,**<font color="green">5.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13205 (**<font color="red">93.4</font>**,46.9)
1. 创业板指: 	 11514 (28.8,28.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 12 (54.5,54.5); 5 (71.4,31.2); 1 (33.3,**<font color="green">7.7</font>**);
    - Low: 9 (**<font color="green">18.2</font>**,**<font color="green">14.5</font>**); 5 (**<font color="green">13.9</font>**,**<font color="green">10.4</font>**); 4 (**<font color="green">12.1</font>**,**<font color="green">11.8</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13205 (**<font color="red">93.4</font>**,46.9)
1. 科创50: 	  2790 (73.1,71.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 3 (27.3,21.4); 2 (66.7,**<font color="green">16.7</font>**); 1 (50.0,**<font color="green">10.0</font>**);
    - Low: 4 (**<font color="green">17.6</font>**,**<font color="green">10.7</font>**); 2 (**<font color="green">16.7</font>**,**<font color="green">8.3</font>**); 2 (**<font color="green">16.7</font>**,**<font color="green">9.1</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1484 (22.6,22.6)
1. 恒生指数: 	 14975 (72.6,58.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 12916 (70.7,73.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 13279 (42.5,**<font color="green">4.6</font>**)
1. 道琼斯指数:	 13049 (43.4,**<font color="green">9.6</font>**)
1. 纳斯达克指数:	  9879 (65.0,29.4)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   778 (25.1,21.0)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
