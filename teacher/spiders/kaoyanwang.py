

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
from teacher.util.shcoolDic import *
class CnkiSpider(scrapy.Spider):
    name = 'kaoyanwang'
    start_urls = ['http://yz.kaoyan.com/']
    mysql=Mysql()
    s_dic=SchoolDic()
    school={}
    def parse(self, response):
        school = response.xpath('//div[@class="collegeList"]/dl/dt/a')
        for s in school:
            link = self.getValue(s.xpath('./@href'),None)
            name = self.getValue(s.xpath('./text()'),None)
            name=self.s_dic.getSchool(name)
            link=self.getLink(link)
            if link is None:
                continue
            self.school[name] = link
        for k in self.school:
            yield scrapy.Request(self.school[k], callback=self.parseLink)
    def parseLink(self, response):
        print(response.url)
        teacher = response.xpath('//ul[@class="subList"]/li/a')
        page=response.xpath("//div[@class='tPage']/a")
        maxPage=self.getMaxPage(page)
        teacherList={}
        for s in teacher:
            link = self.getValue(s.xpath('./@href'),None)
            name = self.getValue(s.xpath('./text()'),None)

            teacherList[name]=link
        for t in teacherList:
            print(t+":"+teacherList[t]+"")
            pattern = re.compile(r'[\s\S]+大学')  # 用于匹配至少一个数字
            m = pattern.match(t)
            print("list"+str(m.group(0)))
    def getMaxPage(self,page):
        list=page.xpath('./text()').extract()
        if len(list)==0:
            return 1

    def getSchool(self,name):
        p1 = re.compile('\s+')
        name = re.sub(p1, ' ', name)
        pass
    def getInstitution(self,name):
        pass
    def getName(self,name):
        pass
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