

from teacher.util.mysql import *
from teacher.util.xin import *
import jieba.posseg as pseg

mysql=Mysql()
xin=Xin()

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
#             mysql.insertTeacherLink(item)

# sql="SELECT a.* from teacherdata2 a inner join (SELECT count(*) as num,name,institution,school,link from `teacherdata2`  GROUP BY name,institution,school having num>2) b on a.name=b.name and a.institution=b.institution and a.school=b.school  ORDER BY b.link"
# list=mysql.get_sql(sql)
# dic={}
# for l in list:
#     if l[2] in dic.keys():
#         dic[l[2]].append(l[0])
#     else:
#         dic[l[2]]=[]
#         dic[l[2]].append(l[0])
#
# for k in dic:
#     lis=dic[k]
#     for li in range(1,len(lis)):
#
#         print(lis[li])
#         mysql.deleteTeacher(lis[li])

sql="select a.name,a.institution,a.school,a.all_link from teacherdata2 a INNER JOIN (select name,institution,school from teacherdata2 where name is not null and name!='' group by name,school,institution) b on a.name=b.name and b.institution=a.institution and b.school=a.school"
list=mysql.get_sql(sql)

for l in list:
    item={}
    item['institution']=l[1]
    item['school']=l[2]
    item['name']=l[0]
    if xin.isXin(l[0])==0:
        continue
    r=mysql.get_teacher(item)
    if len(r)>0:
        pass
    else:
        item['all_link']=l[3]
        print("add:"+str(item))
        mysql.insertTeacher(item)




