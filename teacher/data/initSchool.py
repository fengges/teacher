

from teacher.data.mysql import *
import re
import pandas as pd

mysql=Mysql()
f = open("baikeschool2.txt",'r',encoding='utf8')
line = f.read()
school = eval(line)
data=pd.read_csv("xue_school2.csv")
for a in range(0, data.shape[0]):
    value=data.iloc[a]._values
    if value[0] not in school:
        school[value[0]]={}
    school[value[0]]['province']=value[1]
    school[value[0]]['subjection'] = value[2]
    school[value[0]]['school_type'] = value[3]
    school[value[0]]['level'] = value[4]
    school[value[0]]['characteristic'] = value[5]
    school[value[0]]['graduate'] = value[6]
    school[value[0]]['xuexin_url'] = value[7]
    school[value[0]]['url'] = value[8]

def getString(obj):
    if type(obj)==list:
        s=','.join(obj)
        return s
    else:
        return str(obj)
column = ['abstract', 'image', '英文名', '创办时间', '属性', '校训', '学校地址', '国家重点学科', '硕士点', '博士点','teacher','other']
for s in school:
    for c in column:
        if c not in school[s]:
            school[s][c]=[]
    item={}
    item['name']=s
    item['province']=school[s]['province']
    item['subjection']=school[s]['subjection']
    item['school_type']=school[s]['school_type']
    item['level']=school[s]['level']
    item['characteristic']=school[s]['characteristic']
    item['graduate']=school[s]['graduate']
    item['xuexin_url']=school[s]['xuexin_url']
    item['url']=school[s]['url']

    item['abstract'] = getString(school[s]['abstract'])
    item['logo'] = getString(school[s]['image'])
    item['english_name'] = getString(school[s]['英文名'])
    item['establish'] = getString(school[s]['创办时间'])
    item['attribute'] = getString(school[s]['属性'])
    item['school_motto'] = getString(school[s]['校训'])
    item['address'] = getString(school[s]['学校地址'])
    item['national_disciplines'] = getString(school[s]['国家重点学科'])
    item['master_point'] = getString(school[s]['硕士点'])
    item['doctoral_point'] = getString(school[s]['博士点'])
    item['teacher'] = getString(school[s]['teacher'])
    item['info'] = getString(school[s]['other'])
    for k in item:
        if item[k]!= item[k]:
            item[k]=' '
    try:
        print(item)
        records = {"table": "school_info", "params": item}
        mysql.insertItem(records)
        # mysql.insertSchool(item)
    except:
        print(item)




