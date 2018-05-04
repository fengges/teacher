

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
    name = 'teacher'
    start_urls = ['http://www.baidu.com']
    mysql=Mysql()
    teacher={}
    def parse(self, response):
        list=mysql.getAllTeacher3()
        for l in list:
            self.teacher[str(l[0])]=l
        for k in self.teacher:
            yield scrapy.Request(self.data[k][3], lambda arg1=response, arg2=k: self.parseList(arg1, arg2))

    def parseLink(self, response):
        t={}


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
