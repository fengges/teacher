
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

from minepy import MINE

m = MINE()
x = np.random.uniform(-1, 1, 10000)
m.compute_score(x, x**2)
print m.mic()