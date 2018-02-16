### 以机器学习入门为目的的金价预测

### 数据来源于GLD，最大的以黄金进行直接交易的ETF交易基金

### 机器学习预测黄金价格的步骤：
#### 导入Python库并读取黄金ETF的数据
#### 将数据切分为模型训练数据集和测试数据集
#### 建立线性回归模型
#### 预测黄金ETF的价格

##### python3用到的库： sklearn(LinearRegression)、pandas、numpy、matplotlib、seaborn、fix_yahoo_finance

##### 原始数据图
![](https://github.com/xzshedon/data_analysis/03_study/gold_price_prediction/pic/source.png)
##### 3天，9天均值，x值
![](https://github.com/xzshedon/data_analysis/03_study/gold_price_prediction/pic/s3_s9_avg.png)
##### Y值
![](https://github.com/xzshedon/data_analysis/03_study/gold_price_prediction/pic/pic/y.png)
##### 训练后线性值图：黄线是实际值、蓝线是预测值
![](https://github.com/xzshedon/data_analysis/03_study/gold_price_prediction/pic/linear.png)





###### 仍然有部分不明白的地方,但此次学习的目的重在接触，先有个初步的了解，待后续研究
###### 原文地址： https://mp.weixin.qq.com/s?__biz=MjM5MTQzNzU2NA==&mid=2651657214&idx=1&sn=206923dcb7d470b5de0739b52d2331a2&chksm=bd4c346d8a3bbd7b96de4a000147a8b882f4f9b7fc9fba34b80ac09e6b4b408de234fe3a681d&mpshare=1&scene=1&srcid=0216VDNAk5glxkRAfNhqpmQi&pass_ticket=sPTUUZyiH3BLdMk19XfvjIgEC0lZ44OpFDCan39HBtFyH3u2mNVg00ZdTbugoZ4G#rd