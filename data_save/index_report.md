
## 股指日报 (2023-05-26)

### 总括


#### 恐慌指数 2023-05-26

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	14.86	(30.2,27.8,27.8)
1. 50ETF:	16.18	(46.8,27.9,34.0)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-05-25

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	 10646 (33.4,33.4)
1. 股票:   	 30433 (**<font color="red">100.0</font>**,**<font color="red">100.0</font>**)
1. a股:   	 15273 (76.5,54.1)
1. 上证:   	  7248 (**<font color="red">84.7</font>**,74.2)
1. 上证指数: 	203662 (**<font color="red">90.2</font>**,78.3)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-05-26

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 591 (73.2,**<font color="green">19.0</font>**); 145 (**<font color="green">17.2</font>**,**<font color="green">13.2</font>**); 116 (**<font color="green">17.5</font>**,27.0);
    - Low: 465 (**<font color="green">11.1</font>**,**<font color="green">14.2</font>**); 347 (**<font color="green">12.8</font>**,**<font color="green">13.4</font>**); 279 (20.4,20.7);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-05-25

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.74	(**<font color="green">0.0</font>**,**<font color="green">0.0</font>**,24.0)

![](../data_save\data_img\north_flow_bias_per.png)
