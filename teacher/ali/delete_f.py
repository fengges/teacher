
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


data=pd.read_csv("data/quchujizhi_4.csv")

feature=list(data.columns[1:])
X_all = data[feature]
y_all = label

x=np.array(X_all)
y=np.array(y_all)
t=x[:500]
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor

#Load boston housing dataset as an example


rf = RandomForestRegressor(n_estimators=20, max_depth=4)
scores = []
for i in range(t.shape[1]):
     score = cross_val_score(rf, t[:, i:i+1], y, scoring="r2",
                              cv=ShuffleSplit(len(t), 3, .3))
     scores.append((round(np.mean(score), 3),feature[i]))
print(sorted(scores, reverse=True))