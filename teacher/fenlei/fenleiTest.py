
from teacher.util.mysql import *
mysql=Mysql()
w=open('class2.txt', 'r',encoding='utf-8')
list=w.readlines()
ids=[]
for l in list:
   s=l.split(':')
   ids.append(s[1])
s= input("输入类别")
num=int(s)
while num>=0 and num<=31:
    print('第'+s+'类')
    id=ids[num].split()
    st=''
    for i in id:
        st+=str(i)+','
    st='('+st[0:-1]+')'
    items=mysql.getPaperUrl(st)
    for it in items:
        print(it[0])
    s = input("输入类别")
    num = int(s)
