

import hashlib,pickle
import random,time
import scrapy,copy
from teacher.util.xin import *
from teacher.util.mysql import *
from urllib import parse

class CnkiSpider(scrapy.Spider):
    name = 'baidufanyi'
    start_urls = ['http://www.baidu.com']
    mysql=Mysql()
    dic={}
    def parse(self, response):
        file2 = open('teacher/data/dic.txt', 'rb')
        self.dic = pickle.load(file2)
        self.num = 0
        i = 0
        dic=copy.deepcopy(self.dic)
        for t in dic:
            if dic[t] != 1:
                continue
            url = self.getUrl(t)
            i += 1
            if i % 5000 == 0:

                print("sleep:" + str(i))

            yield scrapy.Request(url, callback=self.parseLink)

    def parseLink(self, response):
        self.num += 1
        if self.num % 5000 == 0:
            print('save:' + str(self.num))
            f = open('teacher/data/dic.txt', 'wb')
            pickle.dump(self.dic, f)
            f.close()
        item = response.xpath('//div[@id="phrsListTab"]')
        try:
            word=item.xpath("./h2/span[@class='keyword']/text()").extract()[0]
        except:
            word=response.url[25:]
            try:
                word2=response.xpath('//div[@class="error-wrapper"]/div[@class="error-typo"]/p/span/a/text()').extract()[0]
            except:
                return
            self.dic[word]=word2
            self.dic[word2]=1
            url = self.getUrl(word2)
            yield scrapy.Request(url, callback=self.parseLink)
            return

        list=item.xpath("./div[@class='trans-container']/ul/li/text()")
        isNandV=False
        for l in list:
            strL=l.extract()
            if strL[0]=="n" or strL[0]=="v":
                cn=strL.split('.')[1].split("；")[0]
                isNandV=True
                self.dic[word] = cn
                break
        if not isNandV and len(list)>0:
            strL = list[0].extract()
            try:
                cn = strL.split('.')[1].split("；")[0]
                self.dic[word] = cn
            except:
                pass



    def parseLink2(self, response):
        try:
            r=eval(response.body)["trans_result"][0]
            self.dic[r['src']]=r['dst']
        except:
            pass

    def getUrl(self, word):

        return "http://dict.youdao.com/w/" +word
    def getUrl2(self,word):
        appid = '20180627000180714'
        secretKey = '9utXpmAO2UyJ8a6MBXdm'
        myurl = '/api/trans/vip/translate'
        q = word
        fromLang = 'en'
        toLang = 'zh'
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        m1 = hashlib.md5()
        m1.update(bytes(sign, encoding="utf8"))
        sign = m1.hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' +parse.quote(q)  + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        return "http://api.fanyi.baidu.com"+myurl


    @staticmethod
    def close(spider, reason):
        print("end:")
        papper={}
        for i in spider.data:
            papper[i]=" ".join([spider.dic[t] for t in spider.data[i]])

        pickle.dump(spider.dic, open('data/dic.txt', 'wb'))
        pickle.dump(papper, open('data/paper.txt', 'wb'))
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)


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

