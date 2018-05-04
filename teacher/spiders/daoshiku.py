

import scrapy
import re
import jieba.posseg as pseg
from teacher.util.xin import *
from teacher.util.mysql import *
from teacher.util.shcoolDic import *
class CnkiSpider(scrapy.Spider):
    name = 'daoshiku'
    start_urls = ['http://www.baidu.com']
    xin=Xin()

    # def parse(self, response):
    #     self.file=open('teacher/data/teacher3.csv','w',encoding='utf8')
    #     self.file.write("学校,学院,姓名,url\n")
    #
    #     start_urls = ['http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&zw=ys',
    #                   'http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&type=211',
    #                   'http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&type=985',
    #                   'http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&xb=nys']
    #     for url in start_urls:
    #         yield scrapy.Request(url, callback=self.parseLink)
    def parse(self, response):
        self.file=open('teacher/data/teacher3.csv','w',encoding='utf8')
        self.file.write("学校,学院,姓名,url\n")

        start_urls = ['http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&zw=ys',
                      'http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&type=211',
                      'http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&type=985',
                      'http://cksp.eol.cn/tutor_search.php?page=1&do=b_search&xb=nys']
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parseLink)
    def parseLink(self, response):
        list=response.xpath('//table[@class="tab_01"]/tr')
        print(response.url)
        for l in range(1,len(list)):
            t=list[l].xpath("./td[1]/nobr/a")
            s = list[l].xpath("./td[2]/nobr/a")
            link=self.getValue(t.xpath('./@href'),None)
            name= self.getValue(t.xpath("./text()"),'')
            sname= self.getValue(s.xpath("./text()"), None)
            self.file.write(sname+', ,'+name+','+link+'\n')
        if self.getPage(response.url) == '1':
            page = response.xpath('//td[@align="center"]/a')
            link = self.getValue(page[-1].xpath("./@href"), None)
            maxPage = self.getPage(link)
            for i in range(1, int(maxPage) + 1):
                url = "http://cksp.eol.cn/tutor_search.php" + self.getPageUrl(link, i)
                yield scrapy.Request(url, callback=self.parseLink)

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