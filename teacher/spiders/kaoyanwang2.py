

import scrapy
import re
import jieba.posseg as pseg
from teacher.util.xin import *
from teacher.util.mysql import *
from teacher.util.shcoolDic import *
import pandas as pd
import numpy as np
class CnkiSpider(scrapy.Spider):
    name = 'kaoyanwang2'
    start_urls = ['http://www.kaoyan.com/']
    xin=Xin()
    data={}
    filter=["姓名","性别","职称","副教授","教授"]
    def parse(self, response):
        data=pd.read_csv("teacher/data/teacher.csv")
        for a in range(0,data.shape[0]):
            self.data[str(a)]=data.iloc[a]._values
        for k in self.data:
            yield scrapy.Request(self.data[k][3], lambda arg1=response, arg2=k: self.parseList(arg1, arg2))


    def parseList(self,response,k):
        node=response.xpath('//div[@class="articleCon"]/table')
        # if response.url=="http://yz.kaoyan.com/sdjtu/daoshi/13/503734/":
        #     print()
        if len(node)!=0:
            value=self.data[k]
            strList=node.xpath('string(.)').extract()
            isFalse=True
            for t in strList:
                t=self.replaceWhite(t)
                s=t.split(" ")
                for a in s:
                    if  len(a)<=10:
                        pass
                    else:
                        isFalse=False

            if not isFalse:
                pass
                # print(response.url)
                # print("too long:"+t)
            else:
                print(response.url)
                print("short:" + t)

    def replaceWhite(self, info):
        p1 = re.compile('\s+')
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