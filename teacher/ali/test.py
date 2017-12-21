
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.model_selection import  train_test_split as test

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
t=d_x[0:500]
t_a=d_x[500:600]
t_b=d_x[600:]
#---------------------测试-----------------------------
sum=0
for  i in range(10):
    X_train, X_test, y_train, y_test = test(t, y, test_size=0.3)
    model = LinearRegression()
    # model.fit(X_train,y_train)

    quadratic_featurizer = PolynomialFeatures(degree=2)
    X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
    X_test_quadratic = quadratic_featurizer.transform(X_test)
    model.fit(X_train_quadratic, y_train)
    predictions = model.predict(X_test_quadratic)
    loss = mse(predictions, y_test)
    print(loss)
print('mean')
print(sum/10)