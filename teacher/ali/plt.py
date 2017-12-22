import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
data=pd.read_csv("data/nan_mean_3.csv")

feature=list(data.columns[1:])
X_all = data[feature]
k=range(721)
i=0
for f in feature:
    f1 = plt.figure(i)
    plt.subplot(211)
    plt.scatter(k,X_all[f])

    savefig('D:/pic/'+f+'.jpg')
    plt.close(i)
    i+=1
    print('pic:'+f+"is done")