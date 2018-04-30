

import scrapy
import codecs
import urllib
import time
import re
import json
from scrapy.http import HtmlResponse
from scrapy.http import XmlResponse
from scrapy.http import Request
from teacher.util.xin import *
from teacher.util.mysql import *
class CnkiSpider(scrapy.Spider):
    name = 'teacherifream'
    start_urls = ['http://www.cnki.net']
    # mysql=Mysql()
    school={}
    url_fill=['about:blank']
    def parse(self, response):
        school = self.mysql.getSchool(1)
        for s in school:
            self.school[str(s[0])] = s
        for k in self.school:
            #     yield scrapy.Request(k,dont_filter=True, callback=self.parseLink)

            yield scrapy.Request(self.school[k][3], lambda arg1=response, arg2=k: self.parseLink(arg1, arg2))

    def parseLink(self, response,k):
        src=response.xpath('//iframe/@src')
        school=self.school[k]
        for s in src:
            url=s.extract()
            link=self.getTeacherUrl(response.url,url)
            if url in self.url_fill:
                continue
            print("link---------------------------------")
            item = {}
            item['school']=school[1]
            item['adpart']=school[2]
            item['url']=link
            print(item)
            self.mysql.insertSchool2(item)



    def getDomain(self,url):
        reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
        m = re.match(reg, url)
        uri = m.groups()[0] if m else ''
        temp=uri[uri.rfind('.', 0, uri.rfind('.')) + 1:]
        index=url.index(temp)+len(temp)
        return url[0:index]
    def getTeacherUrl(self,ins,url):

        domain=self.getDomain(ins)

        url = url.strip()
        if len(url) == 0:
            return ' '
        if url[0:4] == 'http':
            return url
        if url[0] == '/':
            return domain + url
        elif ins[-1] == '/' and url[0] == '.':
            return ins + url
        elif ins[-1] == '/':
            index = ins[0:-1].rfind('/')
            if index == -1:
                l = ins + url
            else:
                l = domain + '/' + url
            return l
        else:
            index = ins.rfind('/')
            return ins[0:index + 1] + url



