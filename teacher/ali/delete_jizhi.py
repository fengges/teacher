

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
data=pd.read_csv("data/time_regular_mean_tool_5.csv")
size=[500,100,121]

feature=list(data.columns[1:])
X_all = data[feature]

time_data=pd.read_csv("data/time_col_4.csv")
feature_time=list(time_data.columns[1:])


x=np.array(X_all)

#-----------------------找到离散变量--------------
l_col=[]
del_col=[]
def getClosed(n,k):
    min=10
    mini=0
    for i in range(len(k)):
        t=(k[i]-n)
        if t<0:
            t=-t
        if t<min:
            min=t
            mini=i
    return k[mini]

for j in range(x.shape[1]):
    col_name = feature[j]
    ind=col_name.lower().find('tool')
    if ind>=0:
        continue
    if col_name in feature_time:
        continue
    dic = {}
    for i in range(x.shape[0]):
        if x[i,j] == x[i,j]:
            s=str(x[i,j])
            if s in dic.keys():
                dic[str(x[i,j])] += 1
            else :
                dic[str(x[i,j])] = 1
    num=0
    sum = 0
    k_list=[]
    for k in dic:
        if dic[k]>50:
            num+=1
            sum+=dic[k]
            k_list.append(float(k))
    r=sum/x.shape[0]
    if r>=0.9:
        if num==1:
            del_col.append(col_name)
        elif num<=7:
            for i in range(x.shape[0]):
                if x[i, j] == x[i, j]:
                    t= x[i, j]
                    if t not in k_list:
                        x[i, j]=getClosed(t,k_list)
            l_col.append(col_name)

df = pd.DataFrame(x, columns=feature)
X_all = df.drop(columns=del_col)
l_df = X_all[l_col]
X_all = X_all.drop(columns=l_col)
col=X_all.columns
#-----------------------整数化----------------

def getClass(X_all,n):
    col=X_all.columns
    cl=[]
    for t in col:
        cl.append(t)
    arr=np.array(X_all)
    a=arr*n
    for c in range(a.shape[0]):
        for r in range(a.shape[1]):
            a[c,r]=int(a[c,r])
    x=pd.DataFrame(a, columns=cl)
    return x

x=np.array(X_all)
y = x.copy()
cla=getClass(X_all,25)
x=np.array(cla)

for j in range(x.shape[1]):
    col_name = col[j]
    ind=col_name.lower().find('tool')
    if ind>=0:
        continue
    if col_name in feature_time:
        continue
    dic = {}
    for i in range(x.shape[0]):
        if x[i,j] == x[i,j]:
            s=str(x[i,j])
            if s in dic.keys():
                dic[str(x[i,j])] += 1
            else :
                dic[str(x[i,j])] = 1
    num=0
    sum = 0
    k_list=[]
    for k in dic:
        if dic[k]>20:
            num+=1
            sum+=dic[k]
            k_list.append(float(k))
    r=sum/x.shape[0]
    if r>=0.9:
        print(col_name)
        for i in range(x.shape[0]):
            if x[i, j] == x[i, j]:
                t= x[i, j]
                if t not in k_list:
                    y[i, j]=getClosed(t,k_list)*1.0/25
    else:
        print(col_name+'---------------')
p = pd.DataFrame(y, columns=col)

p= (p - p.min()) / (p.max() - p.min())
frames=[p,l_df]
result = pd.concat(frames, axis=1)
result.to_csv("data/quchujizhi_4.csv")