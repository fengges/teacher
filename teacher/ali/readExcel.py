
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import  train_test_split as test
#--------------------将特征变为数字--------------------
# data=pd.read_excel("data/训练.xlsx",sheetname=0)
# label=data.columns[-1]
# feature=list(data.columns[1:-1])
# X_all = data[feature]
# y_all = data[label]
#
# def preprocess_features(X):
#     output = pd.DataFrame(index=X.index)
#     for col, col_data in X.iteritems():
#         if col_data.dtype == object:
#             col_data = col_data.replace(['yes', 'no'], [1, 0])
#         if col_data.dtype == object:
#             col_data = pd.get_dummies(col_data, prefix=col)
#         output = output.join(col_data)
#     return output
#
# print(X_all.head())
# X_all = preprocess_features(X_all)
# result = pd.concat([X_all, y_all], axis=1)
# result.to_csv("data/value_1.csv")


#--------------------去除无用特征--------------------
# data=pd.read_csv("data/value_1.csv")
# label=data.columns[-1]
# feature=list(data.columns[1:-1])
# X_all = data[feature]
# y_all = data[label]
# print(X_all.head())
# delete_col=[]
# for i in range(len(X_all.columns)):
#     col_name = X_all.columns[i]
#     col = X_all[col_name]
#     dic = {}
#     for v in col:
#         if v == v:
#             dic[str(v)] = 1
#     if len(dic) <= 1:
#         delete_col.append(col_name)
#         print(X_all.columns[i])
# df = pd.DataFrame(delete_col, columns=['col'])
# df.to_csv("data/delete_cols.csv")
# X_all = X_all.drop(columns=delete_col)
# print(X_all.head())
# result = pd.concat([X_all, y_all], axis=1)
# result.to_csv("data/delete_unuse_feature_2.csv")

#---------------------处理缺省值----------------------
# data=pd.read_csv("data/delete_unuse_feature_2.csv")
# # data=data.fillna(0)
# data=data.fillna(data.mean())
# data.to_csv("data/nan_mean_3.csv")

# df = pd.read_csv('pooja.csv')
# df_norm = (df - df.mean()) / (df.max() - df.min())
# df_norm.to_csv('example.csv')

#---------------------训练预测----------------------

data=pd.read_csv("data/nan_mean_3.csv")
pre_a=pd.read_excel("data/测试A.xlsx")

label=data.columns[-1]
feature=list(data.columns[1:-1])
X_all = data[feature]
y_all = data[label]
x=np.array(X_all)
y=np.array(y_all)

model = LinearRegression()
model.fit(x,y)

predictions = model.predict(X_test)
loss=mse(predictions,y_test)
print(loss/len(y_test))


