

import scrapy
import re
import jieba.posseg as pseg
from teacher.util.xin import *
from teacher.util.mysql import *
from teacher.util.shcoolDic import *
class CnkiSpider(scrapy.Spider):
    name = 'kaoyanwang'
    start_urls = ['http://www.kaoyan.com/']
    xin=Xin()
    s_dic=SchoolDic()
    pageSchool={}
    school={}
    file= open('teacher/data/teacher.csv','w',encoding='utf8')
    split = ["硕士研究生指导教师介绍：","硕士研究生指导教师介绍:","硕士导师介绍：","博士生导师简介:","名师介绍：","教授简介：","研究生老师：","老师介绍：","研究生导师介绍：","研究生导师简介:","导师简介：","硕士生导师：","研究生导师：","博士生导师介绍：","博导介绍：","博士生导师：","导师信息：","硕导介绍：","硕导介绍－","导师介绍：","导师介绍——","导师介绍:","导师："]
    nameRe=[re.compile(r'硕士研究生导师简介\(([\s\S]+)\)'),re.compile(r'硕士生导师简介([\s\S]+)教授'),re.compile(r'硕士生导师简介\(([\s\S]+)\)'),re.compile(r'硕士生导师介绍\(([\s\S]+)\)'),re.compile(r'考研([\s\S]+)老师信息'),re.compile(r'博士生导师([\s\S]+)简历介绍'),re.compile(r'研究生导师介绍([\s\S]+)教授'),re.compile(r'博士生导师([\s\S]+)介绍'),re.compile(r'研究生导师([\s\S]+)介绍'),re.compile(r'研究生导师([\s\S]+)简介'),re.compile(r'考研([\s\S]+)导师信息'),re.compile(r'导师简介\[([\s\S]+)\]'),re.compile(r'导师简介([\s\S]+)教授'),re.compile(r'大学导师([\s\S]+)教授'),re.compile(r'教授([\s\S]+)老师介绍')]
    nameReplace=["介绍","研究员","师范"]
    notName=["马克思","各类专家","特聘教授","广播电视","吉林财经","师范"]
    notInstitution=["拟录取确认","具有招生资格导师名单","研究方向及导师","新增名单","导师基本情况登记表","导师介绍","硕士研究生","博士研究生","导师一览","各院系导师","各院系硕士导师","介绍汇总表","研究生","指导教师","介绍","硕士汇总","汇总",'博士生',"表","博导","考研导师","导师信息","导师简介","导师名单","导师队伍","情况说明","硕士生","硕士","导师","师资队伍简介","名单","简介","部分","招生","队伍"]
    year =re.compile(r'[0-9]+年')
    daxue = re.compile(r'[\s\S]+大学')
    institutionRe=[re.compile(r'学院([\s\S]+学院)'),re.compile(r'[\s\S]+学院'),re.compile(r'[\s\S]+研究所'),re.compile(r'[\s\S]+研究院'),re.compile(r'[\s\S]+实验室'),re.compile(r'[\s\S]+中心'),re.compile(r'[\s\S]+部'),re.compile(r'[\s\S]+学'),re.compile(r'[\s\S]+医院'),re.compile(r'[\s\S]+工程'),re.compile(r'[\s\S]+专业'),re.compile(r'[\s\S]+系'),re.compile(r'[\s\S]+所'),re.compile(r'[\s\S]+站'),re.compile(r'[\s\S]+院'),re.compile(r'[\s\S]+园')]
    # isList=['考研导师队伍','硕士生导师名单','导师名单']
    def parse(self, response):
        self.file.write("学校,学院,姓名,url,type\n")
        area=response.xpath('//ul[@class="yzAreaList"]/li')
        for a in area:
            link=self.getValue(a.xpath("./@rel"),None)
            yield scrapy.Request(link, callback=self.parseArea)

    def parseArea(self, response):
        school={}
        area = response.xpath('//ul[@class="schoolList"]/li/dl/dt/a')
        for a in area:
            link = self.getValue(a.xpath("./@href"), None)
            link = self.getLink(link)
            name = self.getValue(a.xpath("./text()"), None)
            name=name.replace("研究生院",'')
            name=self.s_dic.getSchool(name)
            school[name] = link
            self.school[name] = link
        for k in school:
            yield scrapy.Request(school[k], callback=self.parseLink)

    # def parse(self, response):
    #     school = response.xpath('//div[@class="collegeList"]/dl/dt/a')
    #     for s in school:
    #         link = self.getValue(s.xpath('./@href'),None)
    #         name = self.getValue(s.xpath('./text()'),None)
    #         name=self.s_dic.getSchool(name)
    #         link=self.getLink(link)
    #         if link is None:
    #             continue
    #         self.school[name] = link
    #     for k in self.school:
    #         yield scrapy.Request(self.school[k], callback=self.parseLink)

    def parseLink(self, response):
        # print(response.url)
        teacher = response.xpath('//ul[@class="subList"]/li/a')
        page=response.xpath("//div[@class='tPage']/a")
        school=self.getValue(response.xpath("//h1[@class='subTitleName']/text()"),None)
        school=school[0:-4]

        print("school:"+school)
        teacherList={}
        for s in teacher:
            link = self.getValue(s.xpath('./@href'),None)
            name = self.getValue(s.xpath('./text()'),None)
            teacherList[name]=link
        for t in teacherList:
            r,a=self.getNameAndScool(t)
            inst,nam,isInst=self.getInstitution(school, r[0], t)
            if isInst==False and len(nam) and len(r)<2:
                r.append(nam)
            if len(r)==2:
                try:
                    self.file.write(school+","+inst+","+r[1]+','+teacherList[t]+',1\n')
                except:
                    print(r)
            else:
                self.file.write(school + "," + inst + ", ," + teacherList[t] + ',2\n')
        if response.url.find('.html')<0:
            maxPage=self.getMaxPage(page)
            for i in range(2,int(maxPage)+1):
                url=self.getPageUrl(response.url,i)
                yield scrapy.Request(url, callback=self.parseLink)

    def getPageUrl(self,url,page):
        return url+"index_"+str(page)+'.html'

    def getMaxPage(self,page):
        list=page.xpath('./text()').extract()
        if len(list)>2:
            return list[-2]
        return 0

    def getInstitution(self,school,name,t):
        name = re.sub(self.year, '', name)
        if name.find(school) < 0:
            pass
        else:
            name=name.replace(school,'')
        name=re.sub(self.daxue, '', name)
        m=self.institutionRe[0].search(name)
        if m is not None:
            return m.group(1),'',True
        for i in range(1,len(self.institutionRe)):
            m=self.institutionRe[i].search(name)
            if m is not None:
                return m.group(),'',True
        for a in self.notInstitution:
            name=name.replace(a,'')
        if len(name) != 0:
            if self.isXin(name) == 1:
                return '',name,False
        return name,'',False,

    def isXin(self, inf):
        isName = self.xin.isXin(inf)
        if isName == 1:
            return 1
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
                return 1
        return 0

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

    def getNameByRe(self,name):
        for r in self.nameRe:
            m = r.search(name)
            if m is not None:
                n=m.group(1)
                if n.isdigit():
                    continue
                t=name.replace(m.group(),'')
                return [t,m.group(1)],'re'
        return self.getNameByJieba(name),"jieba"

    def getNameByJieba(self,name):
        seg_list = pseg.cut(name)
        words = []
        for word, flag in seg_list:
            if flag == "nr":
                isName = self.xin.isXin(word)
                if isName == 1 and name not in self.notName:
                    words.append(word)
        s=''
        for i in words:
            name.replace(i,'')
            s+=i+"、"
        if len(s)==0:
            return [name]
        else:
            return [name,s[0:-1]]

    def getNameAndScool(self, name):
        # if name.find('武汉数字工程研究所导师介绍')>=0:
        #     print(name)
        r,a=self.getNameBySplit(name)
        if len(r)<2:
            return r,a
        p1 = re.compile(r'\（[\s\S]+\）')
        name = re.sub(p1, '',r[1])
        for rw in self.nameReplace:
            name= name.replace(rw, '')
        t = name.split("、")
        nlist=[]
        for i in t:
            if i not in self.notName:
                nlist.append(i)
        s=''
        for k in nlist:
            s+=k+"、"
        s=s[0:-1]
        r[1]=s
        return r,a

    def getNameBySplit(self,name):
        ifs=False
        for k in self.split:
            list=name.split(k)
            if len(list)==2:
                ifs=True
                r=list
        if ifs:
            return r,"split"
        else:
            return self.getNameByRe(name)


    def getLink(self,link):
        if link[-1]!="/":
            link = link + '/daoshi/'
        else :
            link=link+'daoshi/'
        return link

    def replaceWhite(self, info):
        p1 = re.compile('\s+')
        # p2=re.compile('[a - zA - Z0 - 9]+')
        # info = re.sub(p2, " ",info)
        new_string = re.sub(p1, ' ', info)
        return new_string

    def getValue(self, node, value):
        if len(node):
            return node.extract()[0]
        else:
            return value

    def getDomain(self,url):
        reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
        m = re.match(reg, url)
        uri = m.groups()[0] if m else ''
        temp=uri[uri.rfind('.', 0, uri.rfind('.')) + 1:]
        index=url.index(temp)+len(temp)
        return url[0:index]

    def getTeacherUrl(self,url):
        url=url.strip()
        if len(url)==0:
            return ' '
        if url[0:4]=='http':
            return url
        if url[0]=='/':
            return self.domain+url
        elif self.url[-1] == '/' and url[0] == '.':
            return self.url+url
        elif self.url[-1]=='/' :
            index = self.url[0:-1].rfind('/')
            if index==-1:
                l=self.url + url
            else :
                l=self.domain+'/'+url
            return l
        else :
            index=self.url.rfind('/')
            return self.url[0:index+1]+url