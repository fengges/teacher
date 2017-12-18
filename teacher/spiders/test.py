

import scrapy
import codecs
import urllib
import time
import re
import json
import traceback
import json
from scrapy.http import Request

class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://www.12371.cn/special/xxzd/jh/']
    items = []

    def parse(self, response):
        self.f = open('text.txt', 'w+', encoding='utf-8')
        list=response.xpath('//ul[@class="showMoreNChildren"]/li/p/a')
        for l in list:
            url=l.xpath('./@href').extract()[0]
            yield scrapy.Request(url, callback=self.parseLink)

    def parseLink(self, response):
        item={}
        passage=response.xpath('//div[@class="word"]/p/text()')
        passStr=''
        for p in passage:
            passStr+=p.extract()
        time=response.xpath('//i[@class="time"]/text()').extract()[0]
        title=response.xpath('//h1[@class="big_title"]/text()').extract()
        item['title']=title[1]
        item['passage'] = passStr
        item['time']=time
        in_json = json.dumps(item,ensure_ascii=False)
        self.f.write(in_json+'\n')
        print(item)
        self.items.append(item)







