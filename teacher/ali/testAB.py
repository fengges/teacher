
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import  train_test_split as test
#--------------------将特征变为数字--------------------
# data=pd.read_excel("data/测试B.xlsx",sheetname=0)
# feature=list(data.columns[1:])
# X_all = data[feature]
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
# X_all.to_csv("data/b_value_1.csv")
# result = pd.concat([X_all, y_all], axis=1)
# result.to_csv("data/value_1.csv")

#--------------------去除无用特征--------------------
data=pd.read_csv("data/b_value_1.csv")
col=pd.read_csv("data/delete_cols.csv")
feature=list(data.columns[1:])
X_all = data[feature]
delete_col=col['col'].tolist()


X_all = X_all.drop(columns=delete_col)
print(X_all.head())
X_all.to_csv("data/b_delete_unuse_feature_2.csv")

#---------------------处理缺省值----------------------
# data=pd.read_csv("data/delete_unuse_feature_2.csv")
# # data=data.fillna(0)
# data=data.fillna(data.mean())
# data.to_csv("data/nan_mean_3.csv")