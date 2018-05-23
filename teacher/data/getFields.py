
from teacher.data.mysql import *
import re
import json
from sklearn.externals import joblib
mysql=Mysql()
#
# list=mysql.getTeacher()
# joblib.dump(list,'teachlist')

list=joblib.load('teachlist')
fieldLabel=['研究方向','研究领域','研究兴趣']
fieldRelist=[r'从事([\s\S]+)等研究',r'从事([\s\S]+)的研究',r'致力于([\s\S]+)等方面的研究工作',r'致力于([\s\S]+)方面的研究工作','致力于([\s\S]+)的研究工作','致力于([\s\S]+)的工作']
fieldRe=[]
fieldName=[ l.strip() for l in open('fields2.txt',encoding='utf8').readlines()]
test={}
for l in fieldRelist:
    fieldRe.append(re.compile(l))
fields={}
def setField(info):
    temp={}
    field = re.split(r'[;,、.，。； ]*', info)
    for f in field:
        if len(f) != 0:
            if f in temp.keys():
                temp[f] += 1
            else:
                temp[f] = 0
    return temp
def updateField(l,fields,field):

    for k in field :
        isNotIn=False
        if k in fieldName:
            isNotIn=True
        if isNotIn==False:
            for f in fieldName:
                if k.find(f)>=0:
                    t=k
                    k=f
                    break
        if len(k)>0 and k not in l['fields']:
            l['fields'].append(k)
    return l,fields
for l in list:
    teacher=eval(l['info'])
    if '研究领域' in teacher.keys():
        a=re.compile(r'\([\s\S]+\)')
        b=re.compile(r'（[\s\S]+）')
        info = a.sub("", teacher['研究领域'])
        info = b.sub("", info)
        l['fields']=[]
        temp= setField(info)
        l,fields=updateField(l,fields,temp)
    else:
        l['fields'] = []
        infoList=teacher['info'].split()
        for info in infoList:
            for fr in fieldRe:
                m = fr.search(info)
                if m is not None:
                    temp = setField(m.group(1))
                    l,fields = updateField(l, fields, temp)
                    info=info.replace(m.group(),'')
        for info in infoList:
            for label in fieldLabel:
                if info.find(label)>=0:
                    index=infoList.index(info)
                    num=1
                    dic={}
                    while index+num<len(infoList) and infoList[index+num][0:5].find(str(num))>=0:
                        f=infoList[index+num]
                        if f in dic.keys():
                            dic[f] += 1
                        else:
                            dic[f] = 0
                        num += 1
                    l, fields = updateField(l, fields, dic)
                    while index + num < len(infoList) and num<=5:


                        f = infoList[index + num]
                        temp = setField(f)
                        # if num == 1:
                        #     for k in temp:
                        #         if k in test.keys():
                        #             test[k] += temp[k]
                        #         else:
                        #             test[k] = temp[k]
                        l, fields = updateField(l, fields,temp)
                        num += 1

# file=open('fields.txt','w',encoding='utf8')
# for k in test:
#     file.write(k+'\n')
# print(fields)


for l in list:
    if len(l['fields'])==0:
        continue
    item={}
    item['id']=l['id']
    item['fields']=','.join(l['fields'])
    print('update:'+str(item['id']))
    mysql.updateTeacher(item)
