
import pandas as pd
import numpy as np
import time
# ----------------找到时间列--------------------
# data=pd.read_csv("data/delete_unuse_feature_2.csv")
# feature=list(data.columns[1:])
# X_all = data[feature]
# t=X_all.mean()
# time_col=[]
# for f in feature:
#     y = '{:.8f}'.format(t[f])
#     index=y.find('2017')
#     if index>=0:
#         temp=X_all[f]
#         for i in temp:
#             y = '{:.8f}'.format(i)
#             index=y.find('2017')
#             if index >= 0:
#                 time_col.append(f)
#                 break
# print(time_col)
# time_data=X_all[time_col]
# df = pd.DataFrame(time_data, columns=time_col)
# df.to_csv('data/time_col_2.csv')

# ----------------时间归一化--------------------
# data=pd.read_csv("data/time_col_2.csv")
# feature=list(data.columns[1:])
# X_all = data[feature]
# x=np.array(X_all)
#
# for i in range(x.shape[0]):
#     for j in range(x.shape[1]):
#         c=x[i,j]
#         if c==c:
#             form=''
#             if c>2000081004311596:
#                 form='%Y%m%d%H%M%S%f'
#             elif c>20000809014252:
#                 form = '%Y%m%d%H%M%S'
#             else :
#                 form = '%Y%m%d'
#             y = '{:.0f}'.format(c)
#             try:
#                 t=time.mktime(time.strptime(y, form))
#                 x[i, j] = t
#             except:
#                 x[i, j]=float("nan")
# df = pd.DataFrame(x, columns=feature)
# for f in  feature:
#     c=df[f]
#     list=c.isnull()
#     if len(list)==0:
#         print(f)
#
# df.to_csv('data/time_col_3.csv')

#------------------------归一化-------------------
# data=pd.read_csv("data/time_col_3.csv")
# feature=list(data.columns[1:])
# X_all = data[feature]
# X_all=X_all.fillna(X_all.mean())
# x=np.array(X_all)
# t=X_all.mean()
# min=np.array(t)
# min_index=np.where(min==min.min())[0][0]
# level=x[:,min_index]
# print(feature[min_index])
# for i in range(x.shape[1]):
#     c=x[:,i]
#     if i!=min_index:
#         x[:,i]=x[:,i]-level
#
#
# df = pd.DataFrame(x, columns=feature)
# df_norm = (df - df.min()) / (df.max() - df.min())
# df_norm.to_csv('data/time_col_4.csv')

#------------------------合并-------------------
data=pd.read_csv("data/quchujizhi_4.csv")
feature=list(data.columns[1:])
X_all = data[feature]

time_data=pd.read_csv("data/time_col_4.csv")
feature_time=list(time_data.columns[1:])
t=time_data[feature_time]

delete_col=[]
for i in range(len(feature_time)):
    col_name = feature_time[i]
    col = t[col_name]
    dic = {}
    for v in col:
        if v == v and v!=0:
            dic[str(v)] = 1
    if len(dic) <= 1:
        delete_col.append(col_name)
print(delete_col)
f_t=[]
for f in feature_time:
    if f in feature:
        f_t.append(f)

X_all = X_all.drop(columns=f_t)
frames=[X_all,t]
result = pd.concat(frames, axis=1)
result=result.drop(columns=delete_col)

result.to_csv('data/delf_time_regular_mean_tool_5.csv')