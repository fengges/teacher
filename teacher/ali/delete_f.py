
import pandas as pd
import numpy as np





data=pd.read_csv("data/quchujizhi_4.csv")
value_data=pd.read_csv("data/ans/ten.csv")

feature=list(data.columns[1:])
value_feature=list(value_data.columns[1:])
X_all = value_data[value_feature]

df_norm = (X_all - X_all.min()) / (X_all.max() - X_all.min())
x=np.array(df_norm)
t=x.transpose()

df = pd.DataFrame(t, columns=feature)

mean=df.mean()
n=0
def_f=[]
for f in feature:
    m=mean[f]
    max=df[f].max()
    ind=f.find('_')
    if m>0.5 or max>0.8 or ind>=0:
        n+=1
    else:
        def_f.append(f)
print(n)
data=data.drop(columns=def_f)
data.to_csv("data/drop_f_1867.csv")
df.to_csv("data/f_norm.csv")

