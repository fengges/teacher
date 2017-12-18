
from teacher.util.mysql import *

mysql=Mysql()
list=mysql.getMeetId()
ids={}
for l in list:
    id=l[1].split(',')
    for i in id:
        ids[i]=1

for k in ids:
    item=mysql.getMeetById(k)
    l=len(item)
    if l==0:
        print(k)