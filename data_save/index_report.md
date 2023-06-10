
## 股指日报 (2023-06-09)

### 总括

#### 恐慌指数 2023-06-09

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.40	(**<font color="green">8.3</font>**,31.0,31.0)
1. 50ETF:	16.48	(**<font color="green">11.9</font>**,**<font color="green">16.3</font>**,23.7)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-08

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  9493 (26.2,26.2)
1. 股票:   	 31926 (**<font color="red">95.2</font>**,**<font color="red">95.9</font>**)
1. a股:   	 13711 (65.2,47.2)
1. 上证:   	  5973 (63.0,62.1)
1. 上证指数: 	172439 (45.2,47.5)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-09

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 403 (41.7,**<font color="green">12.2</font>**); 118 (**<font color="green">13.2</font>**,**<font color="green">9.7</font>**); 84 (**<font color="green">10.4</font>**,**<font color="green">18.3</font>**);
    - Low: 682 (**<font color="green">18.9</font>**,21.4); 385 (**<font color="green">13.7</font>**,**<font color="green">14.8</font>**); 322 (22.8,23.9);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-09

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.04	(41.6,**<font color="green">13.6</font>**,34.3)

![](../data_save\data_img\north_flow_bias_per.png)
