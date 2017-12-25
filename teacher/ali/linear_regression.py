
import pandas as pd
import numpy as np
import time
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.model_selection import  train_test_split as test
from scipy.special import comb
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
size=[500,100,121]
label_data=pd.read_csv("data/label.csv")
label=label_data['label']
#--------------------数据读取,合并--------------------
#
# data=pd.read_excel("data/训练.xlsx",sheetname=0)
# data_pre_a=pd.read_excel("data/测试A.xlsx",sheetname=0)
# data_pre_b=pd.read_excel("data/测试B.xlsx",sheetname=0)
#
# label=data.columns[-1]
# feature=list(data.columns[1:-1])
# X_all = data[feature]
# y_all = data[label]
# label=y_all .tolist()
# y_all = pd.DataFrame(label, columns=['label'])
# feature_a=list(data_pre_a.columns[1:])
# X_a = data_pre_a[feature_a]
# feature_b=list(data_pre_b.columns[1:])
# X_b = data_pre_b[feature_b]
#
# frames = [X_all,X_a,X_b]
# result = pd.concat(frames)
# result.to_csv("data/concat.csv")
# y_all.to_csv("data/label.csv")

#--------------------将特征变为数字--------------------
# data=pd.read_csv("data/concat.csv")
# feature=list(data.columns[1:])
# X_all = data[feature]
#
# def preprocess_features(X):
#     output = pd.DataFrame(index=X.index)
#     for col, col_data in X.iteritems():
#         if col_data.dtype == object:
#             col_data = col_data.replace(['yes', 'no'], [1, 0])
#         s = col.lower()
#         inde=s.find('tool')
#         if inde>=0:
#             col_data = pd.get_dummies(col_data, prefix=col)
#         output = output.join(col_data)
#     return output
#
# print(X_all.head())
# X_all = preprocess_features(X_all)
# X_all.to_csv("data/value_tool_1.csv")


#--------------------去除无用特征--------------------
# data=pd.read_csv("data/value_tool_1.csv")
# feature=list(data.columns[1:])
# X_all = data[feature]
#
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
# X_all.to_csv("data/delete_unuse_feature,tool_2.csv")

#---------------------处理缺省值----------------------
# data=pd.read_csv("data/delete_unuse_feature,tool_2.csv")
# feature=list(data.columns[1:])
# X_all = data[feature]
# # data=X_all.fillna(0)
# data=X_all.fillna(data.mean())
# data.to_csv("data/nan_mean_tool_3.csv")

#---------------------规范化---------------------
# data=pd.read_csv("data/nan_mean_tool_3.csv")
#
# feature=list(data.columns[1:])
# X_all = data[feature]
# df_norm = (X_all - X_all.min()) / (X_all.max() - X_all.min())
# df_norm.to_csv('data/regular_mean_tool_4.csv')

#---------------------训练预测----------------------

data=pd.read_csv("data/quchujizhi_4.csv")

feature=list(data.columns[1:])
X_all = data[feature]
y_all = label

x=np.array(X_all)
y=np.array(y_all)
pca = PCA(n_components=120)
d_x=pca.fit_transform(x)
t=d_x[0:500]
t_a=d_x[500:600]
t_b=d_x[600:]
#---------------------测试-----------------------------
def getDegree(m):
    for n in range(1450):
        i=comb(m+n, m)
        if i>=200000:
            return n-1
# sum=0
# for  i in range(100):
#     X_train, X_test, y_train, y_test=test(t,y, test_size = 0.3)
#     model = LinearRegression(normalize=True)
#     # model.fit(X_train,y_train)
#
#     quadratic_featurizer = PolynomialFeatures(degree=3)
#     X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
#     X_test_quadratic = quadratic_featurizer.transform(X_test)
#     model.fit(X_train_quadratic, y_train)
#     predictions = model.predict(X_test_quadratic)
#
#     loss=mse(predictions,y_test)
#     sum+=loss
#     print(loss)
# print('-----')
# print(sum/100)


model = LinearRegression(normalize=True)
# model.fit(X_train,y_train)
quadratic_featurizer = PolynomialFeatures(degree=3)
X_train_quadratic = quadratic_featurizer.fit_transform(t)
X_a_quadratic = quadratic_featurizer.transform(t_a)
X_b_quadratic = quadratic_featurizer.transform(t_b)
model.fit(X_train_quadratic,y_all)
pre=model.predict(X_train_quadratic)
pre_a = model.predict(X_a_quadratic)
pre_b = model.predict(X_b_quadratic)
loss=mse(pre,y_all)
print(loss)
#--------------------生成答案---------------------------

ans_a_label=pd.read_csv("data/ans_a.csv")
ans_a = pd.DataFrame(pre_a)
frames_a = [ans_a_label,ans_a]
result_a = pd.concat(frames_a, axis=1)
result_a.to_csv("data/ans_a_1.csv")

ans_b_label=pd.read_csv("data/ans_b.csv")
ans_b = pd.DataFrame(pre_b)
frames_b = [ans_b_label,ans_b]
result_b = pd.concat(frames_b, axis=1)
result_b.to_csv("data/ans_b_1.csv")
