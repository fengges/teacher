
import json,re
f = open("baikeschool2.txt",'r',encoding='utf8')
dr = re.compile(r'<[^>]+>', re.S)
line = f.read()
line= dr.sub('', line)
school = eval(line)

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
c1 = sorted(temp.items(), key=lambda x: x[1], reverse=True)
for c in c1:
    print(c[0]+":"+str(c[1]))