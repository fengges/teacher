

import scrapy
import codecs
import urllib
import time
import re
import json
from scrapy.http import Request
class CnkiSpider(scrapy.Spider):
    name = 'xuexin'
    start_urls = ['http://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-0.dhtml']
    school={}
    def parse(self, response):
        self.file = open('teacher/data/xue_school.csv', 'w', encoding='utf8')
        self.file.write("院校名称,院校所在地,院校隶属,院校类型,学历层次,院校特性,研究生院,学信链接\n")
        for i in range(135):
            url='http://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-'+str(20*i)+'.dhtml'
            yield scrapy.Request(url,callback=self.parseLink)

    def parseLink(self, response):
        schools=response.xpath('//div[@class="yxk-table"]/table/tr')

        for i in range(1,len(schools)):
            item={}
            school=schools[i]
            schoolNode=school.xpath('./td[1]/a')
            if len(schoolNode)==0:
                schoolNode=school.xpath('./td[1]')
                item['link']=''
            else:
                schoolLink=schoolNode.xpath('./@href')
                item['link']="http://gaokao.chsi.com.cn"+self.setValue(schoolLink,'')
            schoolName=schoolNode.xpath('./text()')
            item['name']=self.setValue(schoolName,'')
            item['place']=self.setValue(school.xpath('./td[2]/text()'),'')
            item['subjection'] = self.setValue(school.xpath('./td[3]/text()'), '')
            item['type'] = self.setValue(school.xpath('./td[4]/text()'), '')
            item['level'] = self.setValue(school.xpath('./td[5]/text()'), '')
            item['features'] = self.setValue(school.xpath('./td[6]/span[1]/text()'), '')+'-'+self.setValue(school.xpath('./td[6]/span[2]/text()'), '')
            item['graduate'] = len(school.xpath('./td[7]/i'))
            print(item)
            self.file.write(item['name']+','+item['place']+','+item['subjection']+','+item['type']+','+item['level']+','+item['features']+','+str(item['graduate'])+','+item['link']+'\n')

    def setValue(self, node, value):
        if len(node):
            return node.extract()[0].strip()
        else:
            return value

