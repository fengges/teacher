
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.model_selection import  train_test_split as test
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import time
from sklearn.tree import DecisionTreeClassifier as DTC
size=[500,100,121]
label_data=pd.read_csv("data/label.csv")
label=label_data['label']


#-----------------------整数化----------------
# data=pd.read_csv("data/regular_mean_4.csv")
# label_norm = (label - label.min()) / (label.max() - label.min())
# feature=list(data.columns[1:])
# X_all = data[feature]
# y_all = label_norm
#
# def getClass(X_all,n):
#     col=X_all.columns
#     cl=[]
#     for t in col:
#         cl.append(t)
#     arr=np.array(X_all)
#     a=arr*n
#     for c in range(a.shape[0]):
#         for r in range(a.shape[1]):
#             a[c,r]=int(a[c,r])
#     x=pd.DataFrame(a, columns=cl)
#     return x
#
# cla=getClass(X_all,10)
# cla.to_csv("data/cla.csv")

#
data=pd.read_csv("data/cla.csv")
label_norm = (label - label.min()) / (label.max() - label.min())
feature=list(data.columns[1:])
X_all = data[feature]
y_all = label_norm*10
x=np.array(X_all)
x=x[0:500]
y=np.array(y_all)
for i in range(y.shape[0]):
    y[i]=int(y[i])


clf=DTC(criterion='entropy')
clf.fit(x,y)
features=clf.feature_importances_
index = np.where(features>0)

data=pd.read_csv("data/delf_time_regular_mean_tool_5.csv")
col=list(data.columns[1:])
feature=col
X_all = data[feature]
y_all = label

del_col=[]
for c in range(len(col)):
    if c not in index[0] :
        ind=col[c].find('_')
        if ind<0:
            del_col.append(col[c])

X_all = X_all.drop(columns=del_col)
x=np.array(X_all)
y=np.array(y_all)
t=x[0:500]
sum=0
for  i in range(100):

    X_train, X_test, y_train, y_test=test(t,y, test_size = 0.3)
    model = LinearRegression(normalize=True)
    # model.fit(X_train,y_train)

    quadratic_featurizer = PolynomialFeatures(degree=2)
    X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
    X_test_quadratic = quadratic_featurizer.transform(X_test)
    model.fit(X_train_quadratic, y_train)
    predictions = model.predict(X_test_quadratic)

    loss=mse(predictions,y_test)
    sum+=loss
    print(loss)
print(sum/100)

# #--------------------生成答案---------------------------
# #
# ans_a_label=pd.read_csv("data/ans_a.csv")
# ans_a = pd.DataFrame(pre_a)
# frames_a = [ans_a_label,ans_a]
# result_a = pd.concat(frames_a, axis=1)
# result_a.to_csv("data/knn_ans_a_1.csv")
#
# ans_b_label=pd.read_csv("data/ans_b.csv")
# ans_b = pd.DataFrame(pre_b)
# frames_b = [ans_b_label,ans_b]
# result_b = pd.concat(frames_b, axis=1)
# result_b.to_csv("data/knn_ans_b_1.csv")