
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.model_selection import  train_test_split as test
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
size=[500,100,121]
label_data=pd.read_csv("data/label.csv")
label=label_data['label']



data=pd.read_csv("data/regular_mean_4.csv")

feature=list(data.columns[1:])
X_all = data[feature]
y_all = label

x=np.array(X_all)
y=np.array(y_all)
pca = PCA(n_components=700)
d_x=pca.fit_transform(x)
t=x[0:500]
t_a=d_x[500:600]
t_b=d_x[600:]

#----------------------knn测试

sum=0
for i in range(1000):
    X_train, X_test, y_train, y_test=test(t,y, test_size = 0.3)

    uni_knr = KNeighborsRegressor(weights='distance')
    uni_knr.fit(X_train, y_train)
    uni_knr_y_predict = uni_knr.predict(X_test)

    loss=mse(uni_knr_y_predict,y_test)
    sum+=loss
print(sum/1000)




# knr = KNeighborsRegressor(weights='uniform')
# knr.fit(t, y)
# pre_a = knr.predict(t_a)
# pre_b = knr.predict(t_b)
#
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