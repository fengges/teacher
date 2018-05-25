

import scrapy,json,time,re
import pandas as pd

class CnkiSpider(scrapy.Spider):
    name = 'schoolBaike'
    start_urls = ['http://www.kaoyan.com/']
    data={}
    school={}
    count={}
    def parse(self, response):

        data=pd.read_csv("teacher/data/xue_school2.csv")
        for a in range(0,data.shape[0]):
            self.data[str(a)]=data.iloc[a]._values
        for k in self.data:
            name=self.data[k][0]
            url=self.getUrl(name)
            self.count[name]=0
            yield scrapy.Request(url, lambda arg1=response, arg2=name: self.parseSchool(arg1, arg2))

    def getUrl(self,name):
        url='http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key='+name+'&bk_length=600'
        return url
    def parseSchool(self,response,name):
        print(name+":"+str(self.count[name]))
        t=json.loads(response.body)
        if "errno" in t or len(t)==0:
            self.count[name]+=1
            if self.count[name]<=10:
                time.sleep(1)
                yield scrapy.Request(response.url+'&time=2',lambda arg1=response, arg2=name: self.parseSchool(arg1, arg2))
            else:
                self.school[name] =self.getDic(t)
        else:
            self.school[name]=self.getDic(t)

    def parseSchool2(self, response, name):
        t = json.loads(response.body)
        self.school[name] =self.getDic(t)
    @staticmethod
    def close(spider, reason):
        file = open('teacher/data/baikeschool.txt', 'w', encoding='utf8')
        file.write(str(spider.school))
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)
    def getDic(self,t):
        item={}
        try:
            item['wapUrl']=t['wapUrl']
        except:
            item['wapUrl'] = ""

        try:
            item['abstract']=t['abstract']
        except:
            item['abstract'] = ""

        try:
            item['wapUrl']=t['wapUrl']
        except:
            item['wapUrl'] = ""
        try:
            item['image']=t['image']
        except:
            item['image'] = ""

        if "card" in t and len(t['card'])!=0:
            card=t['card']
            for c in card:
                name=c['name']
                item[name]=c['value']
        return item


