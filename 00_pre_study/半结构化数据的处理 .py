# 加载第三方包
import pandas as pd # 数据处理包
import numpy as np # 数值计算包
import json # json文件转换包

# 一个简单的json格式字符串
string1 = '{"name":"Sim","gender":"Male","age":28,"province":"江苏"}'
string2 = '{"name":"Lily","gender":"Feale","age":25,"province":"湖北"}'

# 查看数据类型
type(string)

# 将json格式转换为字典
dict1 = json.loads(string1)
dict2 = json.loads(string2)

type(dict1)

# 将字典数据转换为数据框
pd.DataFrame([dict1,dict2])



string =  '{"name":["Sim","Lily"],"gender":["Male","Feale"],\
            "age":[28,25],"province":["江苏","湖北"]}'
# 转换为数据框            
pd.DataFrame(json.loads(string))


data1 = pd.read_excel(r'C:\Users\Administrator\Desktop\data1.xlsx')
data1.head()

data1.UserBasic[0]


# UserBasic列中的信息拆分到各个变量中
basic = []
for i in data1.UserBasic:
    basic.append(json.loads(i))
    
UserBasic = pd.DataFrame(basic)
UserBasic.head()


# 数据整合到一起
final_data = pd.concat([data1[['Id','Mobile']],UserBasic], axis = 1)
final_data.head()


# 避免循环的方式
trans_data = pd.DataFrame(data1.UserBasic.apply(json.loads))
# 数据整合到一起
final_data = pd.concat([data1[['Id','Mobile']],trans_data], axis = 1)




# 读取数据
data2 = pd.read_excel(r'C:\Users\Administrator\Desktop\data2.xlsx')

# 查看字段CellBehaviorData第一行的信息
data2.CellBehaviorData[0]

# 通过切片的方式去除首尾的中括号
s = data2.CellBehaviorData[0][1:-1]
# 将字符串转换成字典，并取出behavior键
d = json.loads(s)['behavior']
# 将字典转换为数据框
df = pd.DataFrame(d)
df

# 取出phone_num
phone_num = [i['phone_num'] for i in data2.CellBehaviorData.str[1:-1].apply(json.loads)]

# 取出CellBehaviorData字段，并解析为数据框
df = pd.concat([pd.DataFrame(j) for j in [i['behavior'] for i in data2.CellBehaviorData.str[1:-1].apply(json.loads)]])
# 将Id与手机号捆绑
user = pd.concat([pd.Series(phone_num,name = 'phone_num'), data2.Id], axis = 1)

# 以手机号作为数据的关联关联
final_data = pd.merge(df, user, left_on = 'cell_phone_num', right_on='phone_num')
final_data.head()
# 查看数据类型
final_data.dtypes

vars = ['call_cnt','call_in_cnt','call_in_time','call_out_cnt','call_out_time','net_flow','sms_cnt','total_amount']
# 对以上变量进行数据类型转换
df_convert = final_data[vars].apply(lambda x: x.astype('float'))

# 从新完成数据合并
final_data2 = pd.concat([df_convert, final_data.loc[:,~final_data.columns.isin(vars)]], axis = 1)

# 对每个id计算近三个月的平均指标值
stats = final_data2.loc[final_data2.cell_mth.isin(['2017-08','2017-07','2017-06']),:].groupby('Id').aggregate(np.mean)
stats


# 构造空列表，存放CellBehaviorData变量每一行形成的数据框
final_data = []
# 使用zip函数捆绑两列，并使用for循环
for Id,CellBehaviorData in zip(data2.Id, data2.CellBehaviorData):
    # 组装数据框
    mydf = pd.DataFrame(json.loads(CellBehaviorData[1:-1])['behavior'])
    # 将数据框与变量Id组装起来
    final_data.append(pd.concat([pd.Series(np.repeat(Id,mydf.shape[0]), name = 'Id'),mydf], axis = 1))

# 构造最终的数据框    
final_data = pd.concat(final_data)

# 数据类型转换
vars = ['call_cnt','call_in_cnt','call_in_time','call_out_cnt','call_out_time','net_flow','sms_cnt','total_amount']
# 对以上变量进行数据类型转换
df_convert = final_data[vars].apply(lambda x: x.astype('float'))

# 从新完成数据合并
final_data2 = pd.concat([df_convert, final_data.loc[:,~final_data.columns.isin(vars)]], axis = 1)
final_data2
# 对每个id计算近三个月的平均指标值
stats = final_data2.loc[final_data2.cell_mth.isin(['2017-08','2017-07','2017-06']),:].groupby('Id').aggregate(np.mean)
stats