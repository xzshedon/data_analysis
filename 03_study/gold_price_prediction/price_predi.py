# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import fix_yahoo_finance as yf

'''
获取10年间每天黄金ETF的价格数据，并将数据存储在Df中；
移除无效变量（使用dropna函数删除NaN值）；
绘制ETF的收盘价格表；
'''

# read data
Df = yf.download('GLD','2008-01-01','2017-12-31')
# only keep colse colums
Df = Df[['Close']]
# drop rows with missing values
Df = Df.dropna()
# plot the closing price of GLD
Df.Close.plot(figsize=(10,5))   #
plt.ylabel("Gold ETF Prices")   #
# plt.show()    # 图1

'''
定义解释变量
'''
Df['S_3'] = Df['Close'].shift(1).rolling(window=3).mean()
Df['S_9'] = Df['Close'].shift(1).rolling(window=9).mean()
Df = Df.dropna()
x = Df[['S_3', 'S_9']]
x.head()    # 图2

'''
定义因变量
'''
y = Df['Close']
y.head()    # 图3

'''
将数据分割为模型训练数据集和测试数据集
'''
t = .8
t = int(t*len(Df))
x_train = x[:t]
y_train = y[:t]
x_test = x[t:]
y_test = y[t:]

'''
建立线性回归模型
Y = m1*x1 + m2*x2 + C
Gold ETF price = m1 * 3 days moving average + m2 * 9 days moving average + c
'''
linear = LinearRegression().fit(x_train,y_train)
# print("Gold ETF Price = ", round(linear.coef_[0], 2),
#       "* 3 Day Moving Average", round(linear.coef_[1], 2),
#       "* 9 Day Moving Average +", round(linear.intercept_, 2)
#       )
'''
输出为： Gold ETF Price =  1.19 * 3 Day Moving Average -0.2 * 9 Day Moving Average + 0.37
'''

'''
预测黄金ETF价格
'''
predicted_price = linear.predict(x_test)
predicted_price = pd.DataFrame(predicted_price, index=y_test.index,columns=['price'])
predicted_price.plot(figsize=(10, 5))
y_test.plot()
plt.legend(['predicted_price', 'actual_price'])
plt.ylabel('Gold ETF Price')
plt.show()  # 图4

'''
用score函数计算模型的拟合优度
'''
r2_score = linear.score(x[t:], y[t:])*100
r2 = float("{0:2f}".format(r2_score))
print(r2)
'''
模型R平方是94.906768，
R平方总是在0~100%直接，越接近100%，表明该模型越能解释黄金ETF的价格
'''