
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.model_selection import  train_test_split as test
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

size=[500,100,121]
label_data=pd.read_csv("data/label.csv")
label=label_data['label']

data=pd.read_csv("data/quchujizhi_4.csv")

feature=list(data.columns[1:])
X_all = data[feature]
y_all = label
label_norm = (label - label.min()) / (label.max() - label.min())
def getClass(label,n):
    arr=np.array(label)
    a=arr*n
    for c in range(a.shape[0]):
        a[c]=int(a[c])
    return a
cla=getClass(label_norm,100)
x=np.array(X_all)
y=np.array(y_all)

t=x[0:500]
lda = LinearDiscriminantAnalysis(n_components=5000)
lda.fit(t,cla)
d_x = lda.transform(x)
t=d_x[0:500]
t_a=d_x[500:600]
t_b=d_x[600:]

#---------------------测试-----------------------------
#
# sum=0
# for  i in range(100):
#     X_train, X_test, y_train, y_test=test(t,y, test_size = 0.3)
#     model = LinearRegression(normalize=True)
#     # model.fit(X_train,y_train)
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
pre_a = model.predict(X_a_quadratic)
pre_b = model.predict(X_b_quadratic)




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