#/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import json

# 通过pandas读取excel
data1 = pd.read_excel(r'data1.xlsx')

# 获取excel中的数据
data1.head()

# 获取data1中UserBasic[0]这一行的数据，看数据特征，为成对的存在的字符
a = data1.UserBasic[0]

# UserBasic列表中信息拆分到各变量中
basic = []
for i in data1.UserBasic:
    basic.append(json.loads(i))

userbasic = pd.DataFrame(basic)
userbasic.head()

find_all = pd.concat([data1[['Id','Mobile']],userbasic],axis=1)
find_all.head()

# for循环太耗时，避免显式循环，使用apply
trans_data = pd.DataFrame(data1.UserBasic.apply(json.loads))
# 数据整合到一起
find_all_data = pd.concat([data1[['Id','Mobile']],trans_data],axis=1)

print find_all_data


