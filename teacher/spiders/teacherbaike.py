

import scrapy,json,time,re,copy
import pandas as pd
from teacher.util.xin import *
import jieba.posseg as pseg
class CnkiSpider(scrapy.Spider):
    name = 'teacherBaike'
    start_urls = ['http://www.kaoyan.com/']
    xin=Xin()
    school={}
    column=[]
    count={}
    def parse(self, response):
        self.init()
        for k in self.school:
            url=self.school[k]["wapUrl"]
            school=k
            url=url.replace('item','collegeteacher')
            if len(url)<4:
                continue
            yield scrapy.Request(url, lambda arg1=response, arg2=school: self.parseSchool(arg1, arg2))

    def init(self):
        f = open("teacher/data/baikeschool.txt", 'r', encoding='utf8')
        dr = re.compile(r'<[^>]+>', re.S)
        line = f.read()
        line = dr.sub('', line)
        school = eval(line)
        temp_school = copy.deepcopy(school)
        dic = {}
        for t in school:
            s = school[t]
            for k in s:
                if k in dic:
                    if type(s[k]) == list:
                        dic[k].extend(s[k])
                    else:
                        dic[k].append(s[k])
                else:
                    if type(s[k]) == list:
                        dic[k] = s[k]
                    else:
                        dic[k] = [s[k]]
        temp = {}
        for k in dic:
            temp[k] = len(dic[k])
        column = []
        for t in temp:
            if temp[t] > 150:
                column.append(t)
        school = temp_school
        schools = {}
        for s in school:
            schools[s] = {}
            for c in column:
                if c in school[s]:
                    schools[s][c] = school[s][c]
                    school[s].pop(c)
                else:
                    schools[s][c] = " "
            schools[s]['other'] = str(school[s])
        self.school=schools
        self.column=column

    def parseSchool(self,response,school):
        # college-teacher-content
        node = response.xpath('//div[@class="college-teacher-content"]/p/text()')
        info=''
        for n in node:
            info+=n.extract()

        node2 = response.xpath('//div[@class="table-divsion"]/table/tr/td')
        name=''
        dic={}
        for n in node2:
            text=n.extract()
            if text.find('align="middle" valign="center"')>=0:
                dr = re.compile(r'<[^>]+>', re.S)
                name = dr.sub('', text)
                if name not in dic:
                    dic[name]=[]
            else:

                dr = re.compile(r'<[^>]+>', re.S)
                line = dr.sub('', text)
                temp=self.getXin(line)
                if len(name)==0:
                    name='教师'
                    dic[name] = []
                dic[name].append(temp.replace(',','，'))
        self.school[school]['teacher']=str(dic)


    @staticmethod
    def close(spider, reason):
        schools=spider.school
        column=spider.column
        f2 = open("teacher/data/baikeschool2.csv", 'w', encoding='utf8')
        strColumn = 'school'
        for c in column:
            strColumn += ',' + c

        f2.write(strColumn + ',other,teacher\n')
        for s in schools:
            if s == "中南林业科技大学":
                print(s)
            line = s + ''
            for k in column:
                line += ',' + str(schools[s][k]).replace(',', '-|-')
            line += ',' + schools[s]['other'].replace(',', '-|-')
            if 'teacher' in schools[s]:
                line += ',' + schools[s]['teacher'].replace(',', '-|-')
            else:
                line += ', '
            f2.write(line + '\n')
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)

    def getXin(self, inf):
        name = self.xin.getXin(inf)
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
                        isName = self.xin.isXin(word)
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
                name = self.xin.get(inf)
                if name != "":
                    return name
        return inf
