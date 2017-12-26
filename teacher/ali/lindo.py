


import pulp
import pandas as pd
import numpy as np


# 2.326845564      3.454555831



data=pd.read_csv("data/ans/result.csv")
feature=data.columns
x=np.array(data)
x2=[]
for i in range(1,x.shape[1]):
    col=x[:,i]
    s=0
    for c in range(len(col)):
        s=s+col[c]*col[c]-x[c,0]*x[c,0]
    x2.append(s*5000)
    x[:,i]=(x[:,i]-x[:,0])*10000
x2=np.array(x2)
t=pd.DataFrame(x, columns=feature)
t=t.drop(columns=['1'])
test=np.array(t)
test_a=test[0:100]
c=test[-1]
test_b=(x2-c*50)*100
max_y=346
min_y=232

print('model:')

v=''
for i in range(100):
    v+="x"+str(i)+"+"
v=v[:-1]
print('min='+v+';')
#import pulp
thorod=25
for j in range(t.shape[1]):
    v = ''
    for i in range(100):
        v += str(test_a[i,j])+"*x" + str(i) + "+"
    v = v[:-1]
    print(v+" <= "+str(test_b[j]+thorod)+';')
    print(v + " >= " + str(test_b[j]-thorod)+';')

for i in range(100):
    print("x" + str(i) + " <= " + str(max_y)+";")
    print("x" + str(i) + " >= " + str(min_y)+";")
for i in range(100):
    print("@gin(x"+str(i)+");")

print('end')