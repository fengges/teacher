
from teacher.data.mysql import *
import jieba.posseg as pseg
from teacher.util.xin import *

xin = Xin()
mysql=Mysql()
title=["两院院士","国家杰出青年科学基金获得者","长江学者","长江讲座教授","中国科学院院士","中国工程院院士","双聘院士"]

def isXin( inf):
    isName =xin.isXin(inf)
    if isName == 1:
        return 1
    else:
        seg_list = pseg.cut(inf)
        words = []
        try:
            for word, flag in seg_list:
                if flag == "nr":
                    isName = xin.isXin(word)
                    if isName == 1:
                        words.append(word)
        except:
            pass
        if len(words) > 0:
            return 1
    return 0


def getXin( inf):
    name = xin.getXin(inf)
    if name is None:
        return ""
    if name != "":
        return name
    else:
        seg_list = pseg.cut(inf)
        words = []
        try:
            for word, flag in seg_list:
                if flag == "nr":
                    isName =xin.isXin(word)
                    if isName == 1:
                        words.append(word)
        except:
            pass
        if len(words) > 0:
            s = ""
            for w in words:
                s += w + ","
            return s[0:-1]
        else:
            name = xin.get(inf)
            if name != "":
                return name
    return inf
school=mysql.getSchool()
def tfind(s):
    for t in title:
        if t.find(s)>=0:
            return True
    return False
for s in school:
    dic=s['teacher']
    if len(dic)==0:
        continue
    dic=eval(dic)
    if len(dic)==0:
        continue
    else:
        for k in dic:

            if k!="教师":
                teacher=dic[k]
                k = k.strip()
                if tfind(k) and len(teacher)!=0:
                    for t in teacher:
                        print(k+":"+getXin(t))


