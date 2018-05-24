
import json,re,copy
f = open("baikeschool.txt",'r',encoding='utf8')
dr = re.compile(r'<[^>]+>', re.S)
line = f.read()
line= dr.sub('', line)
school = eval(line)
temp_school=copy.deepcopy(school)
dic={}
for t in school:
    s=school[t]
    for k in s:
        if k in dic:
            if type(s[k]) == list:
                dic[k].extend(s[k])
            else:
                dic[k].append(s[k])
        else:
            if type(s[k]) == list:
                dic[k]=s[k]
            else:
                dic[k] = [s[k]]
temp={}
for k in dic:
    temp[k]=len(dic[k])
column=[]
for t in temp:
    if temp[t]>150:
        column.append(t)
school=temp_school
schools={}
for s in school:
    schools[s]={}
    for c in column:
        if c in school[s]:
            schools[s][c]=school[s][c]
            school[s].pop(c)
        else:
            schools[s][c] = " "
    schools[s]['other']=str(school[s])
f2 = open("baikeschool.csv",'w',encoding='utf8')
strColumn='school'
for c in column:
    strColumn+=','+c

f2.write(strColumn+',other\n')
for s in schools:
    if s=="中南林业科技大学":
        print(s)
    line=s+''
    for k in column:
        line+=','+str(schools[s][k]).replace(',','，')
    line+=','+schools[s]['other']
    f2.write(line + '\n')