

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

    def parse(self, response):

        pass

    def parseArea(self, response):
        yield scrapy.Request('', callback=self.parseLink)

    def parseLink(self, response):
        print(response.url)

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