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

w=open('fenci.txt', 'r',encoding='utf-8')
list=w.readlines()
ids=[]
corpus=[]
for l in list:
    s=l.split(':')
    corpus.append(s[1])
    ids.append(s[0])

vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
# word=vectorizer.get_feature_names()#获取词袋模型中的所有词语

#-----------svd 分解----------------
# cla=100
# u, s, v = linalg.svds(tfidf,k=cla)
# claList=[]
# for i in range(cla):
#     item=[]
#     claList.append(item)
# for i in range(u.shape[0]):
#     t=u[i,:]
#     re=np.where(t==np.max(t))
#     claList[re[0][0]].append(ids[i])
# t=0
# wo=open('class.txt','w+',encoding='utf-8')
# for it in claList:
#     wo.write("class "+str(t)+":\n")
#     t+=1
#     for i in it:
#         wo.write(str(i)+',')
#     wo.write('\n')

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from sklearn.cluster import KMeans
from scipy.sparse import csr_matrix, coo_matrix
from sklearn.externals import joblib
from scipy.spatial.distance import cdist
import time
K=range(25,40)
meandistortions=[]
km=open('kmean.txt', 'w+',encoding='utf-8')
km.write(str(10)+':'+str(sum)+'\n')
for k in K:
    print(str(k)+':'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    clf = KMeans(n_clusters=k,n_init=5,max_iter=150,tol=1e-3)
    clf.fit(tfidf)
    sum1=clf.inertia_
    km.write(str(k)+':'+str(sum1)+'\n')
    meandistortions.append(sum1)

plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度')
plt.title(u'用肘部法则来确定最佳的K值')
plt.show()
