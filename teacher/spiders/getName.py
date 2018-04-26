# -*- coding: utf-8 -*-
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
import jieba.posseg as pseg
class CnkiListSpider(scrapy.Spider):
    name = 'getName'
    xin=Xin()
    start_urls = ['http://epe.xjtu.edu.cn']
    mysql=Mysql()
    teacher={}
    len=4


    def parse(self, response):
        teacher=self.mysql.getAllTeacher2()
        for t in teacher:
            if (self.check_chinese(t[1])==False or len(t[1])>4) and t[1].find('·')<0 :
               self.teacher[str(t[0])]=t
        for k in self.teacher:
           yield scrapy.Request(self.teacher[k][4], lambda arg1=response, arg2=k: self.parseLink(arg1, arg2))


    def parseLink(self, response,k):
        print(response.url)
        body=self.getBody(response)
        dr = re.compile(r'<[^>]+>', re.S)
        bodyStr=''
        nameList={}
        for b in body:
            bodyStr+=' ' +b.extract()
        info = dr.sub(' ',bodyStr)
        info=self.replaceWhite(info)
        infoList=info.split(' ')
        for inf in infoList:
            if self.isXin(inf)==1:
                n=self.getXin(inf)
                if len(n)==0:
                    continue
                if n not in nameList.keys():
                    nameList[n]=1
                else:
                    nameList[n]+=1
        name=self.get(nameList)
        l=self.teacher[k]
        item={}
        item['school']=l[3]
        item['institution']=l[2]
        item['institution_url'] = ""
        item['name'] = k
        item['link']=l[4]
        item['all_link'] =l[4]
        self.mysql.insertTeacherLink(item)

    def get(self,nameList):
        if len(nameList)>=1:
            isT=False
            try:
                c1 = sorted(nameList, key=lambda x: x[1], reverse=True)
            except:
                print('')
                pass
            for n in c1:
                if len(n)>1 and len(n)<4:
                    isT=True
                    return n
            if isT==False:
                for n in nameList:
                    return n
        return ''
    def check_chinese(self,check_str):
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                pass
            else :
                return False;
        return True
    def isXin(self,inf):
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
        name=self.xin.getXin(inf)
        if name is None:
            return ""
        if name!="":
            return name
        else:
            seg_list = pseg.cut(inf)
            words = {}
            try:
                for word, flag in seg_list:
                    if flag == "nr":
                        isName = self.xin.isXin(word)
                        if isName == 1 and word not in words.keys():
                            words[word]=1
            except:
                pass
            if len(words) > 0:
                s=""
                for w in words:
                    s+=w+","
                return s[0:-1]
            else :
                name=self.xin.get(inf)
                if name!="":
                    return name
        return inf

    def replaceWhite(self,info):
        p1 = re.compile('\s+')
        # p2=re.compile('[a - zA - Z0 - 9]+')
        # info = re.sub(p2, " ",info)
        new_string = re.sub(p1, ' ', info)
        return new_string

    def setValue(self, node, value):
        if len(node):
            return node.extract()[0]
        else:
            return value

    def getBody(self,response):
        body = response.xpath("//html")
        if len(body)>=2:
            return body
        body=response.xpath("//body")
        if len(body)==0:
            if type(response) == XmlResponse:
                body = response.xpath("//Page")
                return body
            else :
                return response.xpath('//*')
        else :
            return body
    def getDomain(self,url):
        reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
        m = re.match(reg, url)
        uri = m.groups()[0] if m else ''
        temp=uri[uri.rfind('.', 0, uri.rfind('.')) + 1:]
        index=url.index(temp)+len(temp)
        return url[0:index]

    def getKeyValue(self, url, key):
        try:
            index = url.index('?')
            query = url[index + 1:]
            paramList = query.split('&')
            for p in paramList:
                temp = p.split('=')
                if temp[0].lower() == key:
                    return temp[1]
        except:
            print(url)
