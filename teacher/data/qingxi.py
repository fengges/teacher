

from teacher.util.mysql import *
from teacher.util.xin import *
import jieba.posseg as pseg
import pandas as pd
mysql=Mysql()
xin=Xin()
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse
from posixpath import normpath


def myjoin(base, url):
    url1 = urljoin(base, url)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme, arr.netloc, path, arr.params, arr.query, arr.fragment))


# if __name__ == "__main__":
#     print(myjoin("http://www.baidu.com", "abc.html"))
#     print(myjoin("http://www.baidu.com", "/../../abc.html"))
#     print(myjoin("http://www.baidu.com/xxx", "./../../abc.html"))
#     print(myjoin("http://www.baidu.com", "abc.html?key=value&m=x"))


# list=mysql.getAllTeacher2()
#
# for l in list:
#     name=l[1]
#     if name is not None and len(name)>3:
#         seg_list = pseg.cut(name)
#         words = {}
#         isF=False
#         for word, flag in seg_list:
#             if flag == "nr":
#                 isName = xin.isXin(word)
#                 if isName == 1:
#                     isF=True
#                     words[word]=l
#         if isF:
#             mysql.deleteTeacher(l[0])
#         for k in words:
#             item={}
#             item['school']=l[3]
#             item['institution']=l[2]
#             item['institution_url'] = ""
#             item['name'] = k
#             item['link']=l[4]
#             item['all_link'] =l[4]
#             print(item)
#             temp={"table":"teacher2","params":item}
#             mysql.insertItem(temp)


# sql="SELECT count(*) as num,name,institution,school,all_link from `teacher2` a GROUP BY name,institution,school,all_link having num>1 "
# list=mysql.get_sql(sql)
#
# for l in list:
#     item={}
#     item['name']=l[1]
#     item['institution'] = l[2]
#     item['school'] = l[3]
#     item['all_link'] = l[4]
#     ts=mysql.get_teacher(item)
#     r=ts[0]
#     for t in ts:
#         if len(t[3])>0:
#             r=t
#     for t in ts:
#         if t[0]!=r[0]:
#             print(t)
#             mysql.deleteTeacher(t[0])

sql="SELECT count(*) as num,name,institution,school from `teacher2` a GROUP BY name,institution,school having num>1 "
list=mysql.get_sql(sql)

for l in list:
    if len(l[1])==0:
        continue
    item={}
    item['name']=l[1]
    item['institution'] = l[2]
    item['school'] = l[3]
    ts=mysql.get_teacher2(item)
    r=None
    for t in ts:
        if t[7] is None:
            r=t[0]
    if r is None:
        dic={t[0]:mysql.get_url_num(t[5]) for t in ts}
        r= sorted(dic.items(), key=lambda item: item[1])[0][0]
    for t in ts:
        if t[7] is None and r!=t[0]:
            print(t)
            mysql.deleteTeacher(t[0])
#
# sql="SELECT a.*,b.school as s,b.institution_url as u from (SELECT * FROM `teacher2` where institution_url='' ) a join (SELECT institution_url,school from teacher2 where institution_url!='' GROUP BY institution_url ) b on a.school=b.institution_url "
# while True:
#     list=mysql.get_sql(sql)
#     if len(list)==0:
#         break
#     for l in list:
#         item={}
#         item['all_link']=myjoin(l[-1],l[4])
#         item['school'] = l[-2]
#         item['institution_url']=l[-1]
#         item['id'] = l[0]
#         print(item)
#         mysql.updateT(item)
# data=pd.read_csv("teacher.csv")
# for a in range(0, data.shape[0]):
#     l= data.iloc[a]._values
#     for i in range(len(l)):
#         if l[i]!=l[i]:
#             l[i]=''
#     item={}
#     item['institution']=l[1]
#     item['school']=l[0]
#     item['name']=l[2]
#     if l[4]==1 and len(l[2])>0:
#         if len(l[1])>0:
#             r=mysql.get_teacher(item)
#         else:
#             r=mysql.get_teacher2(item)
#     if len(r)>0:
#         pass
#     else:
#         item['all_link']=l[3]
#         print("add:"+str(item))
#         mysql.insertTeacher(item)

# data=pd.read_csv("teacher4.csv")
# for a in range(0, data.shape[0]):
#     l= data.iloc[a]._values
#     for i in range(len(l)):
#         if l[i]!=l[i]:
#             l[i]=''
#     item={}
#     item['institution']=l[1]
#     item['school']=l[0]
#     name=l[2]
#     name=name.strip()
#     name=name.replace(" ",'').replace(" ",'')
#     item['name']=name
#
#     if len(l[2])>0:
#         if len(l[1])>0:
#             r=mysql.get_teacher(item)
#         else:
#             r=mysql.get_teacher2(item)
#     if len(r)>0:
#         pass
#     else:
#         item['all_link']=l[3]
#         print("add:"+str(item))
#         mysql.insertTeacher(item)



