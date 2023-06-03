
## 股指日报 (2023-06-02)

### 总括

#### 恐慌指数 2023-06-01

* 选用**沪深300ETF**期权波动率指数作为整个市场恐慌指数的表征
* 其后另附*上证50ETF、中证500ETF*等的期权波动率指数
* 计算分位数所用的周期长度 (20,60,120)
* 输出：指数-波动率指数-分位数

1. 300ETF:	15.10	(**<font color="green">9.6</font>**,29.5,29.5)
1. 50ETF:	16.58	(22.7,23.9,30.9)

![](../data_save\data_img\qvix_day_300ETF_per.png)


#### 检索量波动 2023-06-01

* 选用多个检索词刻画股市热度
* 计算分位数所用的周期长度 (60,120)
* 输出：检索词-检索量-分位数
* 其后附有*上证50、中证500、创业板*等检索情况

1. 股市:   	  8766 (21.2,21.2)
1. 股票:   	 27286 (**<font color="red">86.3</font>**,**<font color="red">88.5</font>**)
1. a股:   	 10559 (37.8,30.3)
1. 上证:   	  5138 (46.1,48.4)
1. 上证指数: 	164275 (32.2,37.8)

![](../data_save\data_img\bday_SZZS.png)


#### 新高新低分位 2023-06-02

* 20-60-120日的新高新低数, 再对该数量使用周期长度 (60,120) 求取分位数
* 输出：指数-某一周期新高数(分位数)-某一周期新低数(分位数)

1. all
    - High: 533 (63.5,**<font color="green">16.9</font>**); 101 (**<font color="green">5.5</font>**,**<font color="green">7.5</font>**); 79 (**<font color="green">6.2</font>**,**<font color="green">16.9</font>**);
    - Low: 131 (**<font color="green">0.0</font>**,**<font color="green">3.1</font>**); 56 (**<font color="green">0.6</font>**,**<font color="green">1.9</font>**); 41 (**<font color="green">1.4</font>**,**<font color="green">2.7</font>**);

![](../data_save\data_img\hl_legu_all.png)

#### 北向资金流入 2023-06-02

* 北向资金流入与其均线的偏离度
* 计算分位数所用的周期长度 (60,120,200)
* 输出: 累计流入量-偏离度-分位数

purchase:	-0.20	(32.2,**<font color="green">10.5</font>**,31.9)

![](../data_save\data_img\north_flow_bias_per.png)
