
## 股指日报 (2023-08-04)

### 总括

#### 恐慌指数 2023-08-03

> * 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
> * 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	16.97	(36.5,54.6,56.9)
1. 50ETF:	18.33	(37.8,47.9,54.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>


#### 检索量波动 2023-08-03

> * 选用多个检索词刻画股市热度
> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数
> * 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 13506 (**<font color="red">96.6</font>**,48.3)
1. 股票:   	 43817 (**<font color="red">88.3</font>**,**<font color="red">90.6</font>**)
1. a股:   	 13196 (41.3,40.5)
1. 上证:   	  5941 (58.1,56.8)
1. 上证指数: 	174566 (50.8,43.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZZS.png"></img>

1. 牛市:   	   581 (45.4,45.4)
1. 熊市:   	   283 (46.6,38.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_cowbear.png"></img>


#### 新高新低分位 2023-08-03

> * 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 586 (36.9,28.5); 322 (41.3,34.5); 140 (50.6,27.2);
    - Low: 642 (27.3,**<font color="green">19.9</font>**); 147 (**<font color="green">11.2</font>**,**<font color="green">5.4</font>**); 58 (**<font color="green">5.8</font>**,**<font color="green">4.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_all.png"></img>

#### 北向资金流入 2023-08-04

> * 北向资金流入与其均线的偏离度
> * 计算分位数所用的周期长度 (60,120,200)
> * 输出: 累计流入量-偏离度-分位数

purchase:	1.21	(74.7,51.6,52.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\north_flow_bias_per.png"></img>

### 主要指数分析 2023-08-03

包括内地宽基指数、港股指数等

#### 上证50

**上证50期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	16.97	(36.5,54.6,56.9)
1. 50ETF:	18.33	(37.8,47.9,54.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_50ETF_per.png"></img>

**上证50搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13506 (**<font color="red">96.6</font>**,48.3)
1. 上证50: 	  1794 (59.6,60.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_SZ50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. sz50
    - High: 11 (52.4,52.4); 4 (44.4,33.3); 1 (25.0,**<font color="green">10.0</font>**);
    - Low: 3 (**<font color="green">10.7</font>**,**<font color="green">10.7</font>**); 1 (**<font color="green">5.0</font>**,**<font color="green">5.0</font>**); 0 (**<font color="green">0.0</font>**,**<font color="green">0.0</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_sz50.png"></img>

#### 沪深300

**沪深300期权波动率指数**

> * 计算分位数所用的周期长度 (20,60,120)
> * 输出：指数-波动率指数-分位数

1. 300ETF:	16.97	(36.5,54.6,56.9)
1. 50ETF:	18.33	(37.8,47.9,54.9)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\qvix_day_300ETF_per.png"></img>

**沪深300搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13506 (**<font color="red">96.6</font>**,48.3)
1. 沪深300:	  4635 (62.3,62.3)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HS300.png"></img>

**沪深300成分股20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. hs300
    - High: 78 (54.7,54.7); 40 (**<font color="red">80.0</font>**,74.1); 17 (**<font color="red">81.0</font>**,36.2);
    - Low: 11 (**<font color="green">7.8</font>**,**<font color="green">7.0</font>**); 2 (**<font color="green">2.3</font>**,**<font color="green">1.9</font>**); 1 (**<font color="green">1.3</font>**,**<font color="green">1.3</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_hs300.png"></img>

#### 中证500

**中证500搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13506 (**<font color="red">96.6</font>**,48.3)
1. 中证500:	  3891 (67.9,46.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_ZZ500.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. zz500
    - High: 101 (59.1,59.1); 66 (**<font color="red">87.8</font>**,**<font color="red">86.7</font>**); 33 (**<font color="red">100.0</font>**,56.9);
    - Low: 22 (**<font color="green">5.2</font>**,**<font color="green">7.9</font>**); 8 (**<font color="green">3.8</font>**,**<font color="green">4.1</font>**); 4 (**<font color="green">3.1</font>**,**<font color="green">3.4</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_zz500.png"></img>

#### 创业板指

**创业板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13506 (**<font color="red">96.6</font>**,48.3)
1. 创业板指: 	 11147 (21.2,21.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_399006.png"></img>

**20-60-120日的新高新低数**

> * 再对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. cyb
    - High: 17 (77.3,77.3); 7 (**<font color="red">100.0</font>**,43.8); 1 (33.3,**<font color="green">7.7</font>**);
    - Low: 4 (**<font color="green">6.8</font>**,**<font color="green">7.1</font>**); 1 (**<font color="green">2.8</font>**,**<font color="green">2.1</font>**); 1 (**<font color="green">3.0</font>**,**<font color="green">2.9</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_cyb.png"></img>

#### 科创50

**科创板搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 股市:   	 13506 (**<font color="red">96.6</font>**,48.3)
1. 科创50: 	  2740 (68.3,69.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_KC50.png"></img>

**20-60-120日的新高新低数**

> * 对该数量使用周期长度 (60,120) 求取分位数
> * 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. kc50
    - High: 5 (45.5,35.7); 2 (66.7,**<font color="green">16.7</font>**); 1 (50.0,**<font color="green">10.0</font>**);
    - Low: 5 (23.5,**<font color="green">17.2</font>**); 2 (**<font color="green">16.7</font>**,**<font color="green">8.3</font>**); 1 (**<font color="green">8.3</font>**,**<font color="green">4.5</font>**);

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\hl_legu_kc50.png"></img>

#### 恒生

**恒生、恒生科技搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 港股:   	  1553 (26.5,26.5)
1. 恒生指数: 	 15463 (77.2,61.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSI.png"></img>

恒生科技指数:	 12946 (71.4,74.2)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_HSTECH.png"></img>


#### 美股

**美股搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

1. 美股行情: 	 16309 (**<font color="red">85.8</font>**,25.8)
1. 道琼斯指数:	 15276 (72.6,25.4)
1. 纳斯达克指数:	 11733 (**<font color="red">99.9</font>**,50.8)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_IXIC.png"></img>


#### 螺纹钢

**螺纹钢搜索指数**

> * 计算分位数所用的周期长度 (60,120)
> * 输出：检索词-检索量-分位数

螺纹钢:  	   832 (40.2,33.6)

<img width="800" src="c:\Users\84066\Documents\trade_tools\data_save\data_img\bday_RB0.png"></img>
