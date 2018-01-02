


from scipy.stats import pearsonr
from sklearn.feature_selection import f_regression
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import  train_test_split as test
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.linear_model import RandomizedLasso
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

t=x[0:500]
ranks={}
p=[]
for i in range(t.shape[1]):
    p.append(pearsonr(t[:,i],y)[0])
ranks['pearsonr']=p


f_r=f_regression(t,y)
ranks['f_regression']=list(f_r[0])


rf = RandomForestRegressor(n_estimators=20, max_depth=4)
scores = []
for i in range(t.shape[1]):
     score = cross_val_score(rf, t[:, i:i+1], y, scoring="r2",
                              cv=ShuffleSplit(len(t), 3, .3))
     scores.append(round(np.mean(score), 3))
ranks['rfr']=scores


lr = LinearRegression()
rfe = RFE(lr, n_features_to_select=1)
rfe.fit(t,y)
ranks['rfe']=list(rfe.ranking_)



ridge = Ridge(alpha=10)
ridge.fit(t,y )
ranks['rg']=list(ridge.coef_)

rf = RandomForestRegressor(n_estimators=20, max_features=20)
rf.fit(t,y)
ranks['rf']=list(rf.feature_importances_)




value=[]
col=[]
for k in ranks:
    value.append(ranks[k])
    col.append(k)

v=np.array(value)
t=v.transpose()

df = pd.DataFrame(t, columns=col)

df.to_csv('data/ten.csv')

