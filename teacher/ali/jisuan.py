

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
print("import time")
print('import pulp')
print("import pandas as pd")
print("import numpy as np")
print("from sklearn.metrics import mean_squared_error as mse")
print("data=pd.read_csv('data/ans/result.csv')")
print("feature=data.columns")
print("x=np.array(data)")
print("t=x[0:100]")
print("y=x[100]")


#import pulp
thorod=10
print("max=34600")
print("min=10000")
print("for n in range(1000):")
print("  print('start')")
print("  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))")
print('  model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)')
#model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)

for i in range(100):
    print("  x"+str(i)+'= pulp.LpVariable(\'x'+str(i)+'\', lowBound=0)')
# A = pulp.LpVariable('A', lowBound=0, cat='Integer')
# B = pulp.LpVariable('B', lowBound=0, cat='Integer')

v=''
for i in range(100):
    v+="x"+str(i)+"+"
v=v[:-1]
print("  model += "+v+",'profit'")
# model += 30000 * A + 45000 * B,'profit'
v = ''
for i in range(100):
    v += "x" + str(i) + "+"
v = v[:-1]
print("  model += "+v+"-max <=0")
for j in range(t.shape[1]):
    v = ''
    for i in range(100):
        v += str(test_a[i,j])+"*x" + str(i) + "+"
    v = v[:-1]
    print("  model += "+v+" <= "+str(test_b[j]+thorod))
    print("  model += " + v + " >= " + str(test_b[j]-thorod))

for i in range(100):
    print("  model += x" + str(i) + " <= " + str(max_y))
    print("  model += x" + str(i) + " >= " + str(min_y))
# #约束
# model += 3 * A + 4 * B <= 30
# model += 5 * A + 6 * B <= 60
# model += 1.5 * A + 3 * B <= 21
#
print("  model.solve()")
print("  pulp.LpStatus[model.status]")
# model.solve()
# pulp.LpStatus[model.status]
#
print("  xList=[]")
for i in range(100):
    print("  xList.append(x"+str(i)+".varValue)")
# print("Production of Car A = {}".format(A.varValue))
# print("Production of Car B = {}".format(B.varValue))
#
#
# print(pulp.value)
print("  xList=np.array(xList)/100")
print("  max=pulp.value(model.objective)-0.01")
print("  sum=0")
print("  for i in range(t.shape[1]):")
print("     sum+=mse(xList,t[:,i])")
print("  mi=sum-y.sum()")
print("  if mi*mi<min:")
print("     min=mi*mi")
print("     name=str(n)+'.scv'")
print("     print(min)")
print("     df = pd.DataFrame(xList)")
print("     df.to_csv(name)")
print("  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))")

