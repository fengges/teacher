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
    name = 'teacherName'
    xin=Xin()
    start_urls = ['http://epe.xjtu.edu.cn']
    # mysql=Mysql()
    school={}
    len=4

    def parse(self, response):
        school=self.mysql.getSchool(100)
        for s in school:
            self.school[str(s[0])]=s
        for k in self.school:
        #     yield scrapy.Request(k,dont_filter=True, callback=self.parseLink)

            yield scrapy.Request(self.school[k][3], lambda arg1=response, arg2=k: self.parseLink(arg1, arg2))
        # url="http://www.tju.edu.cn/seie/szdw/qrjh/"
        # yield scrapy.Request(url, dont_filter=True, callback=self.parseLink)

    def parseLink(self, response,k):
        print(response.url)
        nameList=[]
        nodePath=[]
        body=self.getBody(response)
        dr = re.compile(r'<[^>]+>', re.S)
        bodyStr=''
        for b in body:
            bodyStr+=' ' +b.extract()
        info = dr.sub(' ',bodyStr)
        info=self.replaceWhite(info)
        infoList=info.split(' ')
        for inf in infoList:
            if self.isXin(inf)==1:
                nameList.append(inf)
                node = self.getNode(inf,body)
                if len(node) == 0:
                    continue
                node = node[0]
                path = self.getPathNode(node)
                nodePath.append(path)

        maxPath,p = self.getMatchPath(nodePath)

        for t in p:
            if len(maxPath)==0:
                break
            teacherList=self.getTeacherList(maxPath,body)
            value=self.getNameValue(teacherList)
            print('value:'+str(value))
            if value<0.2:
                print("错误")
                print(teacherList)
                continue
            elif value>0.5:
                print("正确")
                print(teacherList)
            else :
                print("存疑")
                print(teacherList)
                print("筛选")
                teacherList=self.selectByUrl(teacherList)
                print(teacherList)
            maxPath = self.deleteAndGetMax(maxPath,p)
            self.printAndInsertTeacher(teacherList,k)
        self.mysql.updateSchool(self.school[k][0],1)
        # self.school=self.mysql.getSchool()
        # url=self.school[3]
        # self.url=url
        # print(url)
        # self.domain =self.getDomain(url)
        # yield scrapy.Request(url, callback=self.parseLink)

    def selectByUrl(self,teacherList):
        teacher={}
        for key in teacherList:
            isName = self.isXin(teacherList[key])
            if isName == 1:
                teacher[key]=teacherList[key]
        return teacher

    def printAndInsertTeacher(self,teacherList,id):
        school=self.school[id]

        if school is None:
            raise 0
        for key in teacherList:
            item={}
            item['school']=school[1]
            item['institution']=school[2]
            item['institution_url']=school[3]
            item['name'] = self.getXin(teacherList[key])
            item['link']=key
            item['all_link'] =self.getTeacherUrl(key,school[3])

            self.mysql.insertTeacherLink(item)

    def deleteAndGetMax(self,maxPath,p):
        p[maxPath] = -1
        maxKey = ''
        maxNum = 0
        for key in p:
            if maxNum < p[key]:
                maxNum = p[key]
                maxKey = key
        return maxKey

    def getTeacherList(self,maxPath,body):
        xpath=self.praseXpath(maxPath)
        aList=body.xpath('./'+xpath)
        teacher={}
        for a in aList:
            name=self.setValue(a.xpath('string(.)'),'a').strip()
            aNode=self.findA(a)

            if aNode is None:
                link=str(-1)+name
            else:
                link = self.setValue(aNode.xpath('./@href'),'href')
                if 'javascript:void(0)'==link:
                    link = str(-1) + name
                if link in teacher.keys():
                    isName = self.isXin(name)
                    if isName == 1:
                        teacher[link] +=','+ self.getXin(name)
                else :
                    teacher[link] = self.getXin(name)
        return teacher
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
                s=""
                for w in words:
                    s+=w+","
                return s[0:-1]
            else :
                name=self.xin.get(inf)
                if name!="":
                    return name
        return inf
    def getNameValue(self,teacherList):
        sum=0
        num=0
        for t in teacherList:
            sum+=1
            isName = self.isXin(teacherList[t])
            if isName == 1:
                num+=1
        if sum==0:
            return 0
        else :
            return num/sum

    def getTeacherUrl(self,url,ins):
        domain = self.getDomain(ins)
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

    def praseXpath(self,path):
        xpath=''
        temp=path.split('&')
        ele=temp[0].split(' ')
        cla=temp[1].split(',')
        for  index,val in enumerate(ele):
            if len(val)==0:
                continue
            xpath+="/"+val
            c=cla[index]
            if (len(c)!=0) and (c!=' '):
                xpath+="[@class='"+c+"']"
        return xpath

    def findA(self,node):
        item=self.getElementId(node)
        if item is None:
            return None
        if item[0]=='a' or item[0]=='A':
            href=node.xpath('./@href').extract()
            if len(href)!=0 and href[0]!='#':
                return node
        aEle=self.findNextA(node)
        if len(aEle)==0:
            parent=self.getParent(node)
            return self.findA(parent)
        else:
            return aEle[0]

    def findNextA(self,node):
        aEle=node.xpath("./a[@href!='#' and not(contains(@href,'.edu.cn'))]")
        if len(aEle) == 0:
            aEle = node.xpath("./*/a[not (contains(@href,'.edu.cn')) and @href!='#']")
            if len(aEle) == 0:
                aEle = node.xpath("./*/*/a[not (contains(@href,'.edu.cn')) and @href!='#']")
                return aEle
            else:
                return aEle
        else :
            return aEle

    def getMatchPath(self,nodePath):
        path,p=self.getMaxPath(nodePath)
        if len(path)==0:
            return '',p
        temp=path.split('&')[1]
        if self.len*2>=len(temp) and self.len<=6:
            self.len+=1
            self.getOnePathNode(nodePath)
            return self.getMatchPath(nodePath)
        else :
            return path,p

    def getMaxPath(self,nodePath):
        p={}
        for t in nodePath:
            key=t['path']+'&'+t['class']
            if key in p:
                p[key]+=1
            else :
                p[key] =1
        maxKey=''
        maxNum=0
        for key in p:
            if maxNum<p[key]:
                maxNum=p[key]
                maxKey=key
        return maxKey,p

    def getOnePathNode(self,nodePath):
        for path in nodePath:
            if not path['parent'] is None:
                element = self.getElementId(path['parent'] )
                if not element is None:
                    path['path'] = element[0] + " " + path['path']
                    path['class'] = element[2] + "," + path['class']
                    path['id'] = element[1] + " " + path['id']
                    temp = self.getParent(path['parent'])
                    path['parent'] = temp

    def getPathNode(self,node):
        path={}
        temp=node
        path['node']=temp
        path['parent']=temp
        path['path'] = ''
        path['id']=''
        path['class']=''
        for i in range(1,self.len+1):
            element = self.getElementId(temp)
            if not element is None:
                path['path'] =element[0]+" "+path['path']
                path['class'] = element[2] + "," + path['class']
                path['id'] = element[1]+" "+path['id']
                temp = self.getParent(temp)
                path['parent'] = temp
        return path

    def getElementId(self,node):
        if node is None:
            return None
        cla=self.setValue(node.xpath('./@class'),' ')
        elementStr=str(node.root)
        item=[]
        element=elementStr.split(' ')
        item.append(element[1])
        try:
            temp=element[3]
        except:
            return None
        item.append(temp[0:-1])
        item.append(cla)
        return item

    def getParent(self,node):
        parent = node.xpath("./parent::*")
        if len(parent)==0:
            return None
        else:
            return parent[0]

    def getNode(self,name,body):
        str = "//*[text()='" + name + "']"
        try:
            node = body.xpath(str)
        except:
            name=self.getXin(name)
            return self.getNode(name,body)

        if len(node)==0:
            str = "//*[contains(text(),'" + name + "')]"
            node = body.xpath(str)
            return node
        else :
            return node

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
