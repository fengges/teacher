
from sklearn.dummy import DummyRegressor as DR
from sklearn.ensemble import AdaBoostRegressor as ABR
from sklearn.ensemble import BaggingRegressor as BR
from sklearn.ensemble import ExtraTreesRegressor as ETR
from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.linear_model import HuberRegressor as HR
from sklearn.linear_model import PassiveAggressiveRegressor as PAR
from sklearn.linear_model import RANSACRegressor as RR
from sklearn.linear_model import SGDRegressor as SR
from sklearn.linear_model import TheilSenRegressor as TSR
from sklearn.tree import ExtraTreeRegressor as ETR
from sklearn.tree import DecisionTreeRegressor as DTR
from sklearn.neural_network import MLPRegressor as MR
regressor={}
regressor['DR']=DR()
regressor['ABR']=ABR()
regressor['BR']=BR()
regressor['ETR']=ETR()
regressor['GBR']=GBR()
regressor['RFR']=RFR()
regressor['GPR']=GPR()
regressor['HR']=HR()
regressor['PAR']=PAR()
regressor['RR']=RR(min_samples=10)
regressor['SR']=SR()
regressor['TSR']=TSR()
regressor['ETR']=ETR()
regressor['DTR']=DTR()
regressor['MR']=MR()


import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import  train_test_split as test
import matplotlib.pyplot as plt
label_data=pd.read_csv("data/label.csv")
label=label_data['label']



data=pd.read_csv("data/quchujizhi_4.csv")

feature=list(data.columns[1:])
X_all = data[feature]
y_all = label

t=X_all[0:500]
t_a=X_all[500:600]
t_b=X_all[600:]

#----------------------测试


for k in regressor:
    sum=0
    for i in range(1000):
        X_train, X_test, y_train, y_test=test(t,y_all, test_size = 0.3)

        clf = regressor[k]
        clf.fit(X_train, y_train)
        pre =clf.predict(X_test)

        loss=mse(pre,y_test)
        sum+=loss
    print(k+":"+str(sum/1000))


