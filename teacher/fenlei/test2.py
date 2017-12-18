
from teacher.util.mysql import *
from teacher.fenlei.fenci import FenCi
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
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
#-------------------tdidf---------------
# w=open('fenci.txt', 'r',encoding='utf-8')
# list=w.readlines()
# ids=[]
# corpus=[]
# for l in list:
#     s=l.split(':')
#     corpus.append(s[1])
#     ids.append(s[0])
#
# vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
# transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
# tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
# word=vectorizer.get_feature_names()#获取词袋模型中的所有词语

# wo=open('word.txt','w+',encoding='utf-8')
# for li in word:
#     wo.write(li+'\n')
# weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
# td=open('td_idf.txt','w+',encoding='utf-8')
# list=mysql.getPaperId()
# for l in list:#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
#     for i in range(len(ids)):
#         if ids[i]==str(l[0]):
#             a=tfidf.getrow(i)
#             break
#     print(str(i)+':')
#     s = ''
#     max=-1
#     td = open('F://test1/'+ids[i]+'.sql', 'w+', encoding='utf-8')
#     for j in range(i + 1, tfidf.shape[0]):
#         b = tfidf.getrow(j).transpose()
#         c = a.dot(b)
#         v=float(c.toarray()[0][0])
#         if v>max:
#             max=v
#             item = []
#             item.append(ids[i])
#             item.append(ids[j])
#             item.append(v)
#         if v>=0.3:
#             s += 'insert into paper_dot value(NUll,' + ids[i] + ',' + ids[j] + ',' + str(v) + ',1);\n'
#     if len(s)<10:
#         s+='insert into paper_dot value(NUll,' +item[0] + ',' + item[1] + ',' + str(item[2]) + ',1);\n'
#     td.write(s)
#     td.close()
    # mysql.insert_paper_dot_many(items)

#--------------------lda-----------------------
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import time
w=open('abstract.txt', 'r',encoding='utf-8')
corpus=[]
ids=[]
w=open('fenci.txt', 'r',encoding='utf-8')
list=w.readlines()
for l in list:
   s=l.split(':')
   ids.append(s[0])
   corpus.append(s[1])
stpwrd_dic = open('stop_words.txt', 'rb')
stpwrdlst=stpwrd_dic.readlines()
cntVector = CountVectorizer(stop_words=stpwrdlst)
cntTf = cntVector.fit_transform(corpus)
temp=cntVector.vocabulary_
le=len(temp)
print(le)
print(':' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
lda = LatentDirichletAllocation(n_topics=32,learning_offset=50.,random_state=0)
docres = lda.fit_transform(cntTf)
claList=[]
for i in range(32):
    item=[]
    claList.append(item)
for i in range(docres.shape[0]):
    t=docres[i,:]
    re=np.where(t==np.max(t))
    claList[re[0][0]].append(ids[i])
t=0
wo=open('class2.txt','w+',encoding='utf-8')
for it in claList:
    wo.write(str(t)+":")
    t+=1
    for i in it:
        wo.write(str(i)+' ')
    wo.write('\n')


