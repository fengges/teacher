

import scrapy
import re
import jieba.posseg as pseg
import pandas as pd
from teacher.util.xin import *
from teacher.util.mysql import *
from teacher.util.shcoolDic import *

class CnkiSpider(scrapy.Spider):
    name = 'field'
    start_urls = ['http://xkfl.xhma.com/']
    mysql=Mysql()

    def parse(self, response):
        data = response.xpath('//div[@class="data"]/ul/li')
        for i in range(1,len(data)-1):
            code1 = self.getValue(data[i].xpath("./span/text()"),None)
            name1=self.getValue(data[i].xpath("./a/text()"),None)
            url=self.getValue(data[i].xpath("./a/@href"),None)
            field={"code1":code1,"name1":name1}
            yield scrapy.Request(url, lambda arg1=response, arg2=field: self.parseLink(arg1, arg2))
    def parseLink(self, response,field):
        data = response.xpath('//div[@class="data"]/ul/li')
        for i in range(1,len(data)-1):
            code2 = self.getValue(data[i].xpath("./span/text()"),None)
            url = self.getValue(data[i].xpath("./a/@href"), None)
            if url is None:
                name2 = self.getValue(data[i].xpath("./text()"), None)
                field["code2"] = code2
                field["name2"] = name2
                records = {"table": "field", "params":field}
                self.mysql.insertItem(records)
                continue

            name2=self.getValue(data[i].xpath("./a/text()"),None)

            field["code2"]=code2
            field["name2"]=name2
            records = {"table": "field", "params": field}
            self.mysql.insertItem(records)
            yield scrapy.Request(url, lambda arg1=response, arg2=field: self.parseLink2(arg1, arg2))

    def parseLink2(self, response, field):
        data = response.xpath('//div[@class="data"]/ul/li')
        for i in range(1, len(data) - 1):
            code3 = self.getValue(data[i].xpath("./span/text()"), None)
            name3 = self.getValue(data[i].xpath("./text()"), None)
            field["code3"]=code3
            field["name3"]=name3

            records = {"table": "field", "params": field}
            self.mysql.insertItem(records)

    def getPageUrl(self,url,i):
        url=url[0:url.find('page=')+5]+str(i)+url[url.find('&do='):]
        return url

    def getPage(self,url):
        page=url[url.find('page=')+5:url.find('&do=')]
        return page




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