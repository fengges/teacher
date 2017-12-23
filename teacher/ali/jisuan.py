

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

print('import pulp')
#import pulp

print('model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)')
#model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)

for i in range(100):
    print("x"+str(i)+'= pulp.LpVariable(\'x'+str(i)+'\', lowBound=0, cat=\'Integer\')')
# A = pulp.LpVariable('A', lowBound=0, cat='Integer')
# B = pulp.LpVariable('B', lowBound=0, cat='Integer')

v=''
for i in range(100):
    v+="x"+str(i)+"+"
v=v[:-1]
print("model += "+v+",'profit'")
# model += 30000 * A + 45000 * B,'profit'
max_y=346
min_y=232
thorod=15
for j in range(t.shape[1]):
    v = ''
    for i in range(100):
        v += str(test_a[i,j])+"*x" + str(i) + "+"
    v = v[:-1]
    print("model += "+v+" <= "+str(test_b[j]+thorod))
    print("model += " + v + " >= " + str(test_b[j] - thorod))

for i in range(100):
    print("model += x" + str(i) + " <= " + str(max_y))
    print("model += x" + str(i) + " >= " + str(min_y))
# #约束
# model += 3 * A + 4 * B <= 30
# model += 5 * A + 6 * B <= 60
# model += 1.5 * A + 3 * B <= 21
#
print("model.solve()")
print("pulp.LpStatus[model.status]")
# model.solve()
# pulp.LpStatus[model.status]
#
for i in range(100):
    print("print('x"+str(i)+" = {}'.format(x"+str(i)+".varValue))")
# print("Production of Car A = {}".format(A.varValue))
# print("Production of Car B = {}".format(B.varValue))
#
#
# print(pulp.value(model.objective))