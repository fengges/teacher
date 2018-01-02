
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
from sklearn.cross_decomposition import PLSRegression as PLSR
regressor={}
# regressor['DR']=DR()
# regressor['ABR']=ABR()
# regressor['BR']=BR()
# regressor['ETR']=ETR()
# regressor['GBR']=GBR()
# regressor['RFR']=RFR()
# regressor['GPR']=GPR()
# regressor['HR']=HR()
# regressor['PAR']=PAR()
# regressor['RR']=RR(min_samples=10)
# regressor['SR']=SR()
# regressor['TSR']=TSR()
# regressor['ETR']=ETR()
# regressor['DTR']=DTR()
# regressor['MR']=MR()
regressor['PLSR']=PLSR()


import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import  train_test_split as test
import matplotlib.pyplot as plt
label_data=pd.read_csv("data/label.csv")
label=label_data['label']



data=pd.read_csv("data/drop_f.csv")

feature=list(data.columns[1:])
X_all = data[feature]
y_all = label

t=X_all[0:500]
t_a=X_all[500:600]
t_b=X_all[600:]

#----------------------测试
meandistortions=[]

K=range(2,10)
for k in K:
    sum=0
    for i in range(100):
        X_train, X_test, y_train, y_test=test(t,y_all, test_size = 0.3)

        clf = PLSR(n_components=k)
        clf.fit(X_train, y_train)
        pre =clf.predict(X_test)
        loss=mse(pre,y_test)
        sum+=loss
    meandistortions.append(sum)
    print(str(k)+":"+str(sum/100))

plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel('困惑度')
plt.title('确定最佳分类数')
plt.show()

