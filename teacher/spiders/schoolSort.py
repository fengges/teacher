

import scrapy
import re
import jieba.posseg as pseg
from teacher.util.xin import *
from teacher.util.mysql import *
from teacher.util.shcoolDic import *
class CnkiSpider(scrapy.Spider):
    name = 'schoolSort'
    start_urls = ['https://www.phb123.com/jiaoyu/gx/23961.html','http://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?xkdm=01,02,03,04,05,06']
    school=[]


    def parse(self, response):
        area=response.xpath('//table/tbody/tr')
        for a in area:
            link=[a.xpath("./td[1]/text()").extract()[0].replace("\r","").replace("\n","").replace("\t",""),a.xpath("./td[2]/text()").extract()[0].replace("\r","").replace("\n","").replace("\t",""),a.xpath("./td[3]/text()").extract()[0].replace("\r","").replace("\n","").replace("\t",""),a.xpath("./td[4]/text()").extract()[0].replace("\r","").replace("\n","").replace("\t",""),a.xpath("./td[5]/text()").extract()[0].replace("\r","").replace("\n","").replace("\t","")]
            link[1]=link[1].replace("（","(").replace("）",")")
            self.school.append(link)
        area2=response.xpath('//a[@class="hei14b"]')
        for a in area2:
            link ="http://www.cdgdc.edu.cn/webrms/pages/Ranking/"+ a.xpath('./@href').extract()[0]
            name=a.xpath('./text()').extract()[0]
            yield scrapy.Request(link, lambda arg1=response, arg2=name: self.parseArea(arg1, arg2))

    xueke={}
    level={}
    def parseArea(self, response,name):
        list=[]
        area = response.xpath('//a[@class="hei12"]')
        for a in area:
            link ="http://www.cdgdc.edu.cn/webrms/pages/Ranking/"+ a.xpath('./@href').extract()[0]
            name2=a.xpath('./text()').extract()[0]
            list.append(name2)
            yield scrapy.Request(link, lambda arg1=response, arg2=name2: self.parseArea2(arg1, arg2))
        self.xueke[name]=list

    def parseArea2(self, response,name2):
        area = response.xpath('//table/tr/td[3]/table/tr[4]/td/div/table/tr')
        list=[]
        for a in area:
            td=a.xpath('./td')
            if len(td)==2:
                leve1 = a.xpath('./td[1]/text()').extract()[0]
                school= a.xpath('./td[2]/div/text()').extract()[0].replace("\xa0"," ")
            else:
                school = a.xpath('./td[1]/div/text()').extract()[0].replace("\xa0"," ")
            temp={"level":leve1,"school":school}
            list.append(temp)
        self.level[name2]=list
    def getXueke(self,xueke2):
        for k in self.xueke:
            if xueke2 in self.xueke[k]:
                return k
    @staticmethod
    def close(spider, reason):
        mysql=Mysql()
        level =spider.level
        for l in level:

            xueke2=l.split(" ")[1]
            xueke1=spider.getXueke(l)
            school=level[l]
            for s in school:
                name=s["school"].split(" ")[7]
                t=mysql.getSchoolByName(name)
                temp={}
                temp["xueke1"]=xueke1
                temp["xueke2"] = xueke2
                temp["level"] = s["level"]
                if len(t)==0:
                    temp["school"] = name
                    item = {}
                    item["table"] = "discipline"
                    item["params"] = temp
                    mysql.insertItem(item)
                else:
                    for i in t:
                        temp["school"] = i[0]
                        item={}
                        item["table"]="discipline"
                        item["params"] = temp
                        mysql.insertItem(item)
        # school=spider.school

        # for s in school:
        #     if s[1]!="学校名称":
        #         item={}
        #         item["title"]=s[3]
        #         item["star"]=s[2]
        #         item["scope"]=s[4]
        #         mysql.updateByName(s[1],item)

        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)

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
