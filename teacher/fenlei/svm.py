# from teacher.util.mysql import *
# file = open("e://teacherdata20.sql",encoding='utf-8')
# f = open("e://teacherdata2.sql",'w+',encoding='utf-8')
# mysql=Mysql()
# while 1:
#     line = file.readline()
#     if not line:
#         break
#     ind=line.find("INSERT INTO `teacherdata` VALUES")
#     if ind==0:
#         try:
#             mysql.exe_sql(line)
#         except:
#             f.write(line)
#     else:
#         f.write(line)


from teacher.util.mysql import *
from teacher.fenlei.fenci import FenCi
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import linalg
import numpy as np
# --------- init - fenci-----------
# fenci=FenCi()
# mysql=Mysql()
#
# textList={}
# f=open('fenci.txt','w+',encoding='utf-8')
# list=mysql.getAbstracts()
# size=len(list)
# print(size)
# t=0
# for l in list:
#     t+=1
#     print(t)
#     textList[l[0]]=fenci.filter(l[1])
#     f.write(str(l[0])+':')
#     a = ' '
#     text=a.join(textList[l[0]])
#     f.write(text+'\n')
import  time
print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
w=open('fenci.txt', 'r',encoding='utf-8')
list=w.readlines()
ids=[]
corpus=[]
for l in list:
    s=l.split(':')
    corpus.append(s[1])
    ids.append(s[0])
def getNum(i,ids):
    for index,id in enumerate(ids):
        if i==int(id):
            return index
vectorizer=CountVectorizer(min_df=5)#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
td=vectorizer.fit_transform(corpus)
tfidf=transformer.fit_transform(td)#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵

f=open('label.txt', 'r',encoding='utf-8')
list=f.readlines()
lists=list[0].split(',')
label=[]
for l in lists:
    label.append(int(l))
print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
from sklearn.model_selection import  train_test_split as test
X_train, X_test, y_train, y_test=test(tfidf,label, test_size = 0.3,random_state = 42)
from sklearn.svm import SVC,LinearSVC
# svclf = SVC(kernel = 'linear')
svclf=LinearSVC()
svclf.fit(X_train,y_train)
preds = svclf.predict(X_test)
num = 0
preds = preds.tolist()
for i,pred in enumerate(preds):
    if int(pred) == int(y_test[i]):
        num += 1
print ('precision_score:' + str(float(num) / len(preds)))
print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

