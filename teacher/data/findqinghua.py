import xlwt
import pandas as pd
# teacher=open('清华教师名单.csv','r',encoding='utf8').readlines()
# price=open('国家科学技术进步奖.csv','r',encoding='utf8').readlines()
# file=open('清华国家科学技术奖.csv','w',encoding='utf8')
# name=[t.split(',')[1].replace('"','') for t in teacher]
# # print(name)
# name2=[t.split(',')[5].replace(' ','').replace('\u3000','') for t in price ]
# print(name2)
# for i,n in enumerate(name2):
#     if n in name:
#         file.write(price[i])
# f=open('清华_国家科学技术进步奖.csv','r',encoding='utf8').readlines()
# f2=open('清华_国家科学技术进步奖2.csv','w',encoding='utf8')
# for l in f:
#     t=','.join(l.strip().split('	'))
#     f2.write(t+'\n')


tmp=open('清华名单.txt','r',encoding='utf8').readlines()[1:]
jijin=open('清华_自然基金.csv','r',encoding='utf8').readlines()[1:]
jijin2=open('清华_自然基金2.csv','r',encoding='utf8').readlines()
name=[t.replace('\n','') for t in tmp]
text=pd.read_excel('清华院士团队及其成果.xls',sheetname='sheet1')
# save="""
# 王补宣
# 王崇愚
# 卢强
# 过增元
# 成会明
# 朱静
# 李亚栋
# 李衍达
# 李家明
# 邱勇
# 张希
# 张钹
# 陆建华
# 陈难先
# 欧阳明高
# 范守善
# 周炳琨
# 段文晖
# 南策文
# 柳百新
# 费维扬
# 顾秉林
# 温诗铸
# 雒建斌
# 潘际銮
# 薛其坤
# 王玉明
# 尤政
# 孙家广
# 李三立
# 李龙土
# 李恒德
# 吴建平
# 吴澄
# 金涌
# 金国藩
# 柳百成
# 倪维斗
# 韩英铎
# 蒋洪德
# 戴琼海
# 周济
# """
save="""
柳百成
翁宇庆
"""
save=[t for t in save.split('\n') if len(t)>0]
name={}
for indexs in text.index:
    if text.loc[indexs][1] in save:
        name[text.loc[indexs][1]]=text.loc[indexs][0]
price={}
for line in jijin2:
    item = line.split(',')
    price[item[3]]=item
id=[]
for line in jijin:
    item=line.split(',')
    if item[0] in name:
        id.append(item[1])
id=(list(set(id)))
yuanshi={}
xuebu=['工程与材料科学部','信息科学部','化学科学部']
dic={i:[] for i in id}
for line in jijin:
    item=line.split(',')
    if item[1]=='51532003':
        print('dd')
    if item[1] in dic:
        # if item[0] in name:
        #     dic[item[1]].append(item[0]+'(院士)')
        # else:
        #     dic[item[1]].append(item[0])
        dic[item[1]].append(item[0])
    if item[0] in name and item[1] in price:
        if item[0] not in yuanshi:
            yuanshi[item[0]]={}
        if price[item[1]][6] not in yuanshi[item[0]]:
            yuanshi[item[0]][price[item[1]][6]]=[]
        yuanshi[item[0]][price[item[1]][6]].append(item[1])

row = 0

for teacher in yuanshi:
    for y in yuanshi[teacher]:
        p=yuanshi[teacher][y]
        team=[]
        for i in p:
            names=dic[i]
            team.extend(names)
        for line in jijin:
            item=line.split(',')
            if item[2] in team and item[1] in dic and  item[1] not in yuanshi[teacher][y] and item[1] in price and price[item[1]][6]==y:
                yuanshi[teacher][y].append(item[1])

for teacher in yuanshi:
    y_dic = {}
    for y in yuanshi[teacher]:
        p = yuanshi[teacher][y]
        for i in p:
            names=price[i][7]
            y_dic[names]=i
    yuanshi[teacher]={}
    for k in y_dic:
        if price[y_dic[k]][6] not in yuanshi[teacher]:
            yuanshi[teacher][price[y_dic[k]][6]]=[]
        yuanshi[teacher][price[y_dic[k]][6]].append(y_dic[k])

y_t={}
for teacher in yuanshi:
    y_t[teacher] = {}
    for y in yuanshi[teacher]:
        p=yuanshi[teacher][y]
        y_t[teacher][y]=p
        team=[]
        for i in p:
            if i in  price and float(price[i][2])>=200 and price[i][5] in xuebu:
                team.append(i)
        yuanshi[teacher][y]=team

row = 0
print(yuanshi)
wbk = xlwt.Workbook(encoding='utf-8')
sheet = wbk.add_sheet('sheet1')
for teacher in yuanshi:
    for y in yuanshi[teacher]:
        p=yuanshi[teacher][y]
        sheet.write(row, 0, name[teacher])
        sheet.write(row, 1, teacher)
        sheet.write(row, 2, y)

        team=[]
        tmp=y_t[teacher][y]
        for t in tmp:
            names = dic[t]
            team.extend(names)
        t_price=[]
        for i in p:
            names=dic[i]
            t_price.append('，'.join(price[i][7:-1]))

        dic_name={}
        for t in team:
            if t in dic_name:
                dic_name[t]+=1
            else:
                dic_name[t]=1
        team=[n+"("+str(v)+")" for n,v in dic_name.items()]
        sheet.write(row, 3,'，'.join(set(team)))
        sheet.write(row, 4,'国家科学自然基金:'+'，'.join(t_price))
        sheet.write(row, 5, len(y_t[teacher][y]))
        row += 1
wbk.save('清华院士团队及其成果4.xls')
from numpy import NaN
row = 0
wbk = xlwt.Workbook(encoding='utf-8')
sheet = wbk.add_sheet('sheet1')
file_tmp=pd.read_excel('937.xlsx',sheetname='Sheet1')
list_973=[[j for j in file_tmp.loc[i]] for i in file_tmp.index]
text1=pd.read_excel('清华院士团队及其成果_合并.xls',sheetname='sheet1')
name_973={file_tmp.loc[i][1]:file_tmp.loc[i][0][0:4] for i in file_tmp.index}
name_price={'，'.join(price[i][7:-1]):price[i] for i in price}
for indexs in text1.index:
        if text1.loc[indexs][8] is NaN:
            name=[]
        else:
            name=text1.loc[indexs][8].split(',')
        id=[]
        n=0
        for line in jijin:
            item=line.split(',')
            if item[2] in name or item[0] in name:
                n+=1
                if item[1] in  price and float(price[item[1]][2])>=200 and price[item[1]][5] in xuebu:
                    id.append('，'.join(price[item[1]][7:-1]))
        t_973=[tmps[1] for tmps in list_973 if tmps[2].replace(' ','') in name ]
        tmp = ''
        if len(t_973)>0:
            sort_973=sorted({t:name_973[t] for t in t_973}.items(),key = lambda x:x[1],reverse = True )
            t_973=[t[0]+' ('+t[1]+')' for t in sort_973]
            tmp='973计划：\n'+'\n'.join(t_973)+'\n'
        if len(id)>0:
            sort_jijin=sorted({t:name_price[t][6] for t in id}.items(),key = lambda x:x[1],reverse = True)
            id=[t[0]+' ('+t[1]+') '+str(int(float(name_price[t[0]][2])))+"万元" for t in  sort_jijin]
            tmp+='国家科学自然基金：\n'+'\n'.join(id)
        sheet.write(row, 0, text1.loc[indexs][0])
        sheet.write(row, 1, text1.loc[indexs][1])
        sheet.write(row, 2, text1.loc[indexs][2])
        sheet.write(row, 3, text1.loc[indexs][3])
        sheet.write(row, 4, '973计划：'+str(len(t_973))+',国家科学自然基金：'+str(n))
        sheet.write(row, 5, '')
        sheet.write(row, 6,tmp)


        row += 1
wbk.save('清华院士团队及其成果_合并3.xls')


test_name=[]
# file=open('清华院士_自然基金.csv','w',encoding='utf8')
#
# for line in jijin2:
#     item=line.split(',')
#     if item[3] in dic:
#         file.write(line.replace('\n','')+','+'-'.join(dic[item[3]])+'\n')
# file.close()

# row = 0
# wbk = xlwt.Workbook(encoding='utf-8')
# sheet = wbk.add_sheet('sheet1')
# for line in jijin2:
#     item=line.split(',')
#     if item[3] in dic:
#
#         sheet.write(row, 0, item[0])
#         sheet.write(row, 1, item[1])
#         sheet.write(row, 2, item[2])
#         sheet.write(row, 3, item[3])
#         sheet.write(row, 4, item[4])
#         sheet.write(row, 5, item[5])
#         sheet.write(row, 6, item[6])
#         sheet.write(row, 7, '，'.join(item[7:-1]))
#         sheet.write(row, 8, item[-1])
#         sheet.write(row, 9, '，'.join(dic[item[3]]))
#
#         row += 1
# wbk.save('清华院士_自然基金.xls')



