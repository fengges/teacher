

import scrapy
import codecs
import urllib
import time
import re
import json
import pandas as pd
from scrapy.http import Request

class CnkiSpider(scrapy.Spider):
    name = 'xuexin2'
    start_urls = ['http://www.baidu.com']
    school={}
    def parse(self, response):
        data = pd.read_csv('teacher/data/xue_school.csv')
        for a in range(0, data.shape[0]):
            l = data.iloc[a]._values
            name=l[0]
            self.school[name]=l.tolist()
            url=l[7]
            if url==url:
                # url='http://gaokao.chsi.com.cn/sch/schoolInfoMain--schId-398215.dhtml'
                yield scrapy.Request(url, lambda arg1=response, arg2=name: self.parseLink(arg1, arg2))

    def parseLink(self, response,name):
        try:
            link = response.xpath( '//div[contains(@class,"yxk-yxmsg")]/div[@class="mid"]/div[@class="msg"]/span[@class="judge-empty"]').extract()[0]
            p1 = re.compile('\s+')
            link = re.sub(p1, '',link)
            p = re.compile('<[^>]+>')
            link=p.sub("",link)
            link=self.replace_chinese(link)
            link=link.replace('http：//','http://')
            wwwindex=link.find('www')
            while wwwindex>=0:
                if wwwindex>=7 and link[wwwindex-7:wwwindex]!='http://':
                    link=link[0:wwwindex]+'http://'+link[wwwindex:]
                elif wwwindex<7:
                    link = link[0:wwwindex] + 'http://' + link[wwwindex:]
                t=wwwindex
                wwwindex=link[wwwindex+3:].find('www')
                if wwwindex<0:
                    break
                else:
                    wwwindex+=t+3

        except Exception as e:
            print(e)


            print('error')
            # print(link)
            print(response.url)
            link = ' '
        print('-------------------')
        urlRe = re.compile('((ht|f)tps?):\/\/[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?$')
        m = urlRe.search(link)

        if m is not None:
            url=m.group()
            httpIndex=url[2:].find('http')
            if httpIndex>=0:
                url=url[0:httpIndex+2]
            print(url)
            self.school[name].append(url)
            self.school[name].append(1)
        else:
            print('fail: '+link)
            self.school[name].append(link)
            self.school[name].append(0)
        print(response.url)
        # print(link)

    @staticmethod
    def close(spider, reason):
        file = open('teacher/data/xue_school2.csv', 'w', encoding='utf8')
        file.write("院校名称,院校所在地,院校隶属,院校类型,学历层次,院校特性,研究生院,学信链接,学校链接,isurl\n")
        for k in spider.school:
            t = spider.school[k]
            for i in range(len(t)):
                if t[i]!=t[i]:
                    t[i]=' '
            if len(t)==10:
                file.write(t[0] + ',' + t[1] + ',' + t[2] + ',' + t[3] + ','+ t[4] + ',' + t[5]  + ',' + str(t[6]) +','+ t[7] + ',' + t[8] + ',' + str(t[9]) + '\n')
            else:
                try:
                    file.write(t[0] + ',' + t[1] + ',' + t[2] + ',' + t[3] + ',' + t[4] + ',' + t[5] + ',' + str(t[6]) + ','+t[7]  + ', , \n')
                except:
                    print(t)
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)

    def replace_chinese(self,check_str):
        s=''
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                pass
            else:
                s+=ch
        return s

    def setValue(self, node, value):
        if len(node):
            return node.extract()[0].strip()
        else:
            return value
