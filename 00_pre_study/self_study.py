#/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import json

string1 = '{"name":"Sim","gender":"Male","age":28,"province":"江苏"}'
string2 = '{"name":"Lily","gender":"Feale","age":25,"province":"湖北"}'

print type(string1)

# 将json字符串转换为字典 json.loads

dict1 = json.loads(string1)
dict2 = json.loads(string2)

print type(dict1)

# 将字典数据转换为数据框

a = pd.DataFrame([dict1,dict2])

print a

string3 = '{"name":["Sim","Lily"],"gender":["Male","Feale"],"age":[28,25],"province":["江苏","湖北"]}'
# 转换为数据框

b = pd.DataFrame(json.loads(string3))
print b



