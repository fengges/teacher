

import scrapy
import codecs
import urllib
import time
import re
import json
import traceback
from scrapy.http import HtmlResponse
from scrapy.http import XmlResponse
from scrapy.http import Request
from teacher.util.xin import *
from teacher.util.mysql import *
class CnkiSpider(scrapy.Spider):
    name = 'teacherhtml'
    start_urls = ['http://www.baidu.com']
    mysql=Mysql()
    teacher={}
    def parse(self, response):
        list=self.mysql.getAllTeacher3()
        file= open('teacher/data/school2.txt', encoding='gbk', mode='r')
        school=[s.strip() for s in file.readlines()]
        for l in list:
            url=l[10]
            if url.find('http://yz.kaoyan.com')<0 and url.find("http://www.chinakaoyan.com")<0 and l[4] in school:
                self.teacher[str(l[0])]=l
        for k in self.teacher:
            try:
                yield scrapy.Request(self.teacher[k][10], lambda arg1=response, arg2=k: self.parseLink(arg1, arg2))
            except:
                pass
        # url="http://cksp.eol.cn/tutor_detail.php?id=25"
        # k=0
        # yield scrapy.Request(url, lambda arg1=response, arg2=k: self.parseLink(arg1, arg2))
    def parseLink(self, response,k):
        teacher=self.teacher[k]
        t={}
        t['name']=teacher[1]
        t['school'] = teacher[4]
        t['instition'] = teacher[5]
        t['url'] = teacher[10]
        if response.url.find("http://cksp.eol.cn/tutor_detail.php")<0:
            try:
                info = response.body.decode()
            except Exception as e:
                print(e)
                info= response.body.decode('gbk')
            # print(info)
            clear = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
            info = clear.sub(" ", info)
            clear = re.compile('<\s*[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
            info = clear.sub(" ", info)
            p = re.compile('<[^>]+>')
            info=p.sub("",info)
            info = self.replaceWhite(info)

            t['info']=str({'info':info})
        else:
            sex=self.setValue(response.xpath("//table[@class='tab_02']/tr[1]/td[2]/text()"),' ')
            birth= self.setValue(response.xpath("//table[@class='tab_02']/tr[1]/td[3]/text()"), ' ')
            zhicheng=self.setValue(response.xpath("//table[@class='tab_02']/tr[3]/td[1]/text()"), ' ')
            zhuanye = self.setValue(response.xpath("//table[@class='tab_02']/tr[3]/td[2]/a/text()"), ' ')
            field = self.setValue(response.xpath("//table[@class='tab_02']/tr[4]/td[1]/text()"), ' ')

            email =self.setValue(response.xpath("//table[@class='tab_01']/tr[1]/td[2]/text()"),' ')
            phone= self.setValue(response.xpath("//table[@class='tab_01']/tr[1]/td[4]/text()"), ' ')
            youbian=self.setValue(response.xpath("//table[@class='tab_01']/tr[1]/td[6]/text()"), ' ')
            address = self.setValue(response.xpath("//table[@class='tab_01']/tr[2]/td[2]/text()"), ' ')

            biref=self.setValue(response.xpath("//div[@id='short_intro']/text()"), ' ')
            award = self.setValue(response.xpath("//div[@id='short_award']/text()"), ' ')
            thesis = self.setValue(response.xpath("//div[@id='short_thesis']/text()"), ' ')
            item={}
            item["性别"]=sex
            item["出生年月"] = birth
            item["职称"] = zhicheng
            item["招生专业"] =zhuanye
            item["研究领域"] = field
            item["E-mail"] = email
            item["电话"] = phone
            item["邮编"] = youbian
            item["地址"] = address
            item["个人简介"] = biref
            item["获得奖项"] = award
            item["著作及论文"] = thesis
            t['info'] = str(item)
        # print(t)
        # self.mysql.insertteacherdata_info(t)
    def getBody(self,response):
        body = response.xpath("//html")
        if len(body)>=2:
            return body
        body=response.xpath("//body")
        if len(body)==0:
            if type(response) == XmlResponse:
                body = response.xpath("//Page")
                if len(body)==0:
                    body = response.xpath("//resume")
                return body
            else :
                return response.xpath('//*')
        else :
            return body

    def replaceWhite(self, info):
        p1 = re.compile('\s+')

        new_string = re.sub(p1, ' ', info)
        return new_string

    def setValue(self, node, value):
        if len(node):
            return node.extract()[0]
        else:
            return value
