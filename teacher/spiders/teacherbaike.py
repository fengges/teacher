

import scrapy,json,time
import pandas as pd

class CnkiSpider(scrapy.Spider):
    name = 'teacherBaike'
    start_urls = ['http://www.kaoyan.com/']
    data={}
    school={}
    count={}
    def parse(self, response):

        url='https://wapbaike.baidu.com/collegeteacher/%E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6/137673'
        name='东南大学'
        yield scrapy.Request(url, lambda arg1=response, arg2=name: self.parseSchool(arg1, arg2))
    def getUrl(self,name):
        url='http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key='+name+'&bk_length=600'
        return url
    def parseSchool(self,response,name):
        # college-teacher-content
        node = response.xpath('//div[@class="college-teacher-content"]/p/string(.)')

        node = response.xpath('//div[@class="table-divsion"]/p/string(.)')
    #     table-divsion

    @staticmethod
    def close(spider, reason):
        file = open('teacher/data/baikeschool.txt', 'w', encoding='utf8')
        file.write(str(spider.school))
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)
