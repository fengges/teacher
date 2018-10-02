

import scrapy
from teacher.util.xin import *

class CnkiSpider(scrapy.Spider):

    name = 'guojia'
    # start_urls = [
    #     # "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm?year=2000"
    #     "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2001/200802/t20080214_59030.htm?year=2001",
    # ]
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table[@class="MsoNormalTable"]/tbody/tr')
    #     level = '一等奖'
    #     for td in tr:
    #         t = td.xpath('./td')
    #         if len(t) < 2:
    #             t_level = td.xpath('./p/b/span/text()').extract()
    #             if len(t_level)>0:
    #                 level=t_level[0]
    #                 print(level)
    #         else:
    #                 priceList = t.xpath('./p')
    #
    #                 o = []
    #                 for a in priceList:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "项目名称" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp) < 4:
    #                     tmp_t = tmp[0]
    #                     tmp = last
    #                     tmp[3] = tmp_t
    #                 else:
    #                     last = tmp
    #                 try:
    #                     teacher = tmp[3].split('、')
    #                 except:
    #                     pass
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     tmsname=te.split(" ")
    #                     if len(tmsname)>=2 and len(tmsname[-1])>3:
    #                         te=''.join(tmsname[0:-1])
    #                     if len(te.replace(' ',''))>4:
    #                         continue
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(isT)+','+str(year) + ',' + level + ',' + os   + '\n')
    # start_urls = [
    #     "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2002/jbj/jbjml.htm?year=2002",
    # ]
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table/tr[2]/td/div/table/tr/td/div/font/*')
    #     level = '一等奖'
    #     for td in tr:
    #         t = td.xpath('./tr')
    #         if len(t) == 0:
    #             t_level = td.xpath('./text()').extract()
    #             if len(t_level)>0:
    #                 level=t_level[0]
    #                 print(level)
    #         else:
    #             priceList = td.xpath('./tr')
    #             for line in priceList:
    #                 tds = line.xpath('./td')
    #                 o = []
    #                 for a in tds:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "主要完成人、主要完成单位" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp) < 2:
    #                     tmp_t = tmp[0]
    #                     tmp = last
    #                     tmp[3] = tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[3].split('、')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     tmsname=te.split(" ")
    #                     if len(tmsname)>=2 and len(tmsname[-1])>3:
    #                         te=''.join(tmsname[0:-1])
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(year) + ',' + level + ',' + os + ',' + str(isT) + '\n')

    # start_urls = [
    #     "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2003/jbj/jbjml.htm?year=2003",
    # ]
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table/tr[2]/td/div/table/tr/td/div/font/*')
    #     level = '一等奖'
    #     for td in tr:
    #         t = td.xpath('./tr')
    #         if len(t) == 0:
    #             t_level = td.xpath('./text()').extract()
    #             if len(t_level)>0:
    #                 level=t_level[0]
    #                 print(level)
    #         else:
    #             priceList = td.xpath('./tr')
    #             for line in priceList:
    #                 tds = line.xpath('./td/p')
    #                 o = []
    #                 for a in tds:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "项目编号,项目名称" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp) < 2:
    #                     tmp_t = tmp[0]
    #                     tmp = last
    #                     tmp[3] = tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[2].split('、')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     os = ','.join(tmp[0:2]) + ',' + te + ',' + ','.join(tmp[3:])
    #                     file.write(str(isT)+','+str(year) + ',' + level + ',' + os + '\n')
    # start_urls = [
    #     "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2004/jb/jb.htm?year=2004",
    # ]
    #
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table[2]/tr[2]/td/table/tr/td/*')
    #     level = '一等奖'
    #     for td in tr:
    #         t = td.xpath('./tr')
    #         if len(t) == 0:
    #             level = td.xpath('string(.)').extract()[0].strip()
    #             print(level)
    #         else:
    #             priceList = td.xpath('./tr')
    #             for line in priceList:
    #                 tds = line.xpath('./td')
    #                 o = []
    #                 for a in tds:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "序号,编号" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp) < 2:
    #                     tmp_t = tmp[0]
    #                     tmp = last
    #                     tmp[3] = tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[3].split('、')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     tmsname=te.split(" ")
    #                     if len(tmsname)>=2 and len(tmsname[-1])>3:
    #                         te=''.join(tmsname[0:-1])
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(year) + ',' + level + ',' + os + ',' + str(isT) + '\n')
    # start_urls = [
    #     "http://www.nosta.gov.cn/2005jldh/jb/jb.htm?year=2005"
    # ]
    #
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table[2]/tr[2]/td/table/tr/td/*')
    #     level='一等奖'
    #     for td in tr:
    #         t = td.xpath('./font')
    #         if len(t) > 0:
    #             level = t.xpath('string(.)').extract()[0].strip()
    #             print(level)
    #         else:
    #             priceList = td.xpath('./tr')
    #             for line in priceList:
    #                 tds = line.xpath('./td/p')
    #                 o = []
    #                 for a in tds:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "序号,编号" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp) < 2:
    #                     tmp_t = tmp[0]
    #                     tmp = last
    #                     tmp[3] = tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[3].split('、')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(isT) +','+str(year) + ',' + level + ',' + os + '\n')
    # start_urls = [
    #     # "http://www.nosta.gov.cn/2006jldh/jb/jb.htm?year=2006",
    # ]
    #
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table[2]/tr[2]/td/table/tr/td/*')
    #     for td in tr:
    #         t = td.xpath('./font')
    #         if len(t) > 0:
    #             level = t.xpath('string(.)').extract()[0].strip()
    #             print(level)
    #         else:
    #             priceList = td.xpath('./table/tr')
    #             for line in priceList:
    #                 tds = line.xpath('./td/p')
    #                 o = []
    #                 for a in tds:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "序号,编号" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp) < 2:
    #                     tmp_t = tmp[0]
    #                     tmp = last
    #                     tmp[3] = tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[3].split('、')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(year) + ',' + level + ',' + os + ',' + str(isT) + '\n')
    # start_urls = [
    #     "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2007/jldh07jlgg/200801/t20080108_58277.htm?year=2007",
    # ]
    #
    # def parse(self, response):
    #
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//div[@id="Zoom"]/*')
    #     for td in tr:
    #         t = td.xpath('./span/text()')
    #         if len(t) >0:
    #             level=t.extract()[0]
    #             print(level)
    #         else:
    #             priceList=td.xpath('./table/tbody/tr')
    #             for line in priceList:
    #                 tds=line.xpath('./td/p')
    #                 o=[]
    #                 for a in tds:
    #                     result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "序号,编号" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp)<2:
    #                     tmp_t=tmp[0]
    #                     tmp=last
    #                     tmp[3]=tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[3].split('，')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(isT) + ',' + str(year) + ',' + level + ',' + os + '\n')
    start_urls = [

                     "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2008/jldh08jlgg/200901/t20090109_66659.htm?year=2008",
                  ]

    def parse(self, response):
        index = response.url.find('year=') + 5
        year = response.url[index:]
        file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
        file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')

        tr = response.xpath('//div[@id="Zoom"]/*')
        for td in tr:
            t = td.xpath('./b[1]/span/text()')
            if len(t) >0:
                level=t.extract()[0]
                print(level)
            else:
                priceList=td.xpath('./table[@class="MsoNormalTable"]/tbody/tr')
                for line in priceList:
                    tds=line.xpath('./td/p')
                    o=[]
                    for a in tds:
                        result = self.replaceWhite(''.join(a.xpath('string(.)').extract())).strip()
                        if len(result) > 0:
                            o.append(result)
                    other = ','.join(o)
                    if len(other) == 0 or "序号,编号" in other:
                        continue
                    isT = 0
                    if other.find('清华') > 0:
                        isT = 1
                    tmp = other.split(',')
                    if len(tmp)<2:
                        tmp_t=tmp[0]
                        tmp=last
                        tmp[3]=tmp_t
                    else:
                        last = tmp
                    teacher = tmp[3].split('，')

                    for te in teacher:
                        if len(te) == 0:
                            continue
                        os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
                        file.write(str(isT) + ',' + str(year) + ',' + level + ',' + os + '\n')

    # start_urls = [
    #     "http://localhost/static/P020100112447134382767.htm?year=2009"
    # ]
    #
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//div[@class="WordSection1"]/*')
    #     for td in tr:
    #         t = td.xpath('./span')
    #         if len(t) >0:
    #             price=t[-1]
    #             try:
    #                 level=price.xpath('./text()').extract()[0]
    #             except:
    #                 pass
    #         else:
    #             priceList=td.xpath('./tr')
    #             for line in priceList:
    #                 tds=line.xpath('./td')
    #                 o=[]
    #                 for a in tds:
    #                     tmps = a.xpath('./p/span')
    #                     result = self.replaceWhite(''.join(tmps.xpath('string(.)').extract())).strip()
    #                     if len(result) > 0:
    #                         o.append(result)
    #                 other = ','.join(o)
    #                 if len(other) == 0 or "序号,编号" in other:
    #                     continue
    #                 isT = 0
    #                 if other.find('清华') > 0:
    #                     isT = 1
    #                 tmp = other.split(',')
    #                 if len(tmp)<2:
    #                     tmp_t=tmp[0]
    #                     tmp=last
    #                     tmp[3]=tmp_t
    #                 else:
    #                     last = tmp
    #                 teacher = tmp[3].split('，')
    #
    #                 for te in teacher:
    #                     if len(te) == 0:
    #                         continue
    #                     os = ','.join(tmp[0:3]) + ',' + te + ',' + ','.join(tmp[4:])
    #                     file.write(str(year) + ',' + level + ',' + os + ',' + str(isT) + '\n')

    # start_urls = [
    #                 "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2010/jldh10jlgg/201101/t20110115_84315.htm?year=2010",
    #                 # "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2011/jldh11jlgg/201202/t20120210_92343.htm?year=2011",
    #               ]
    #
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #
    #     tr = response.xpath('//table[@class="MsoNormalTable"]/tbody/tr')
    #     i=0
    #     for td in tr:
    #         t=td.xpath('./td')
    #         if len(t)<6:
    #             try:
    #                 level=t.xpath('./p/span[1]/text()').extract()[0].replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    #             except:
    #                 try:
    #                     level = t.xpath('./p/b/span[1]/text()').extract()[0].replace('\n', '').replace('\t', '').replace('\r','').replace(' ', '')
    #                 except:
    #                     pass
    #         else:
    #             i+=1
    #             if i==16:
    #                 pass
    #             o=[]
    #             for a in t:
    #                 tmps=a.xpath('./p')
    #                 result=self.replaceWhite(''.join(tmps.xpath('string(.)').extract())).strip()
    #                 if len(result)>0:
    #                     o.append(result)
    #             other=','.join(o)
    #             if len(other)==0 or "序号,编号" in other:
    #                 continue
    #             isT=0
    #             if other.find('清华')>0 :
    #                 isT=1
    #             tmp=other.split(',')
    #             if len(tmp)==5:
    #                 teacher=['']
    #             else:
    #                 teacher=tmp[3].split('，')
    #             for te in teacher:
    #                 if len(te)==0:
    #                     continue
    #                 os=','.join(tmp[0:3])+','+te+','+','.join(tmp[4:])
    #                 file.write(str(year)+','+level+','+os+','+str(isT)+'\n')

    # start_urls = [
    #                 "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2012/jldh12jlgg/201301/t20130117_99203.htm?year=2012",
    #                'http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2013/jldh13jlgg/201401/t20140107_111218.htm?year=2013',
    #               'http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2014/jldh14jlgg/201501/t20150107_117320.htm?year=2014',
    #               'http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2015/jldh15jlgg/201601/t20160106_123351.htm?year=2015',
    #               'http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2016/jldh16jlgg/201701/t20170105_130203.htm?year=2016'
    #               ]
    #
    # def parse(self, response):
    #     index = response.url.find('year=') + 5
    #     year = response.url[index:]
    #     file = open('teacher/data/' + str(year) + '国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #     tr = response.xpath('//table/tbody/tr')
    #     for td in tr:
    #         t=td.xpath('./td')
    #         if len(t)<6:
    #             try:
    #                 level=t.xpath('./p/span[1]/text()').extract()[0].replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    #             except:
    #                 level = t.xpath('./p/b/span[1]/text()').extract()[0].replace('\n', '').replace('\t', '').replace('\r',
    #                                                                                                                '').replace(
    #                     ' ', '')
    #         else:
    #             o=[]
    #             for a in t:
    #                 tmps=a.xpath('./p/span')
    #                 o.append(self.replaceWhite(''.join(tmps.xpath('string(.)').extract())))
    #             other=','.join(o)
    #             if len(other)==0 or other=='序号,编号,项目名称,主要完成人,主要完成单位,推荐单位':
    #                 continue
    #             isT=0
    #             if other.find('清华')>0 :
    #                 isT=1
    #             tmp=other.split(',')
    #             teacher=tmp[3].split('，')
    #             for te in teacher:
    #                 if len(te)==0:
    #                     continue
    #                 os=','.join(tmp[0:3])+','+te+','+','.join(tmp[4:])
    #                 file.write(str(year)+','+level+','+os+','+str(isT)+'\n')

    # start_urls = ['http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm?year=2000']
    # def parse(self, response):
    #     index=response.url.find('year=')+5
    #     year=response.url[index:]
    #     file = open('teacher/data/'+str(year)+'国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人主要完成单位,推荐单位\n')
    #     tr=response.xpath('//table[@class="MsoTableGrid"]/tbody/tr')
    #     level="一等奖"
    #     for td in tr:
    #         other=','.join(td.xpath('./td/p').extract()).replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    #         dr = re.compile(r'<[^>]+>', re.S)
    #         other = dr.sub('',other)
    #         isT=0
    #         if other.find('清华')>0 and year>2012:
    #             isT=0
    #
    #         file.write(str(year)+','+level+','+other+','+str(isT)+'\n')
    # start_urls = ['http://www.nosta.gov.cn/web/detail1.aspx?menuID=163&contentID=1442']
    # def parse(self, response):
    #     year = 2017
    #     file = open('teacher/data/'+str(2017)+'国家科学技术进步奖.csv', 'w', encoding='utf8')
    #     file.write('year,level,序号,编号,项目名称,主要完成人,主要完成单位,推荐单位\n')
    #     tr=response.xpath('//td[@class="content"]/div/table/tbody/tr')
    #     for td in tr:
    #         t=td.xpath('./td')
    #         if len(t)<6:
    #             level=t.xpath('string(.)').extract()[0].replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    #         else:
    #             other=','.join(t.xpath('./p/text()').extract()).replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    #             if len(other)==0:
    #                 continue
    #             isT=0
    #
    #             if other.find('清华')>0 and year>2012:
    #                 isT=1
    #             tmp=other.split(',')
    #             teacher=tmp[3].split('，')
    #             for te in teacher:
    #                 if len(te)==0:
    #                     continue
    #                 os=','.join(tmp[0:3])+','+te+','+','.join(tmp[4:])
    #                 file.write(str(year)+','+level+','+os+','+str(isT)+'\n')

    # start_urls = ['http://www.nosta.gov.cn/web/detail.aspx?menuID=145&contentID=762']
    # def parse(self, response):
    #     t=response.xpath('//table[5]/tr[1]/td[2]/table[5]/tr/td')
    #     area=t.xpath('string(.)').extract()[0].split('\n')
    #     area=[a.strip('\t').strip('\r').strip() for a in area]
    #     area=[a for a in area[2:] if len(a)>0]
    #     file=open('teacher/data/国家最高科学技术奖.csv', 'w', encoding='utf8')
    #     file.write("year,name,birth,desc,is\n")
    #     for a in area:
    #         index=a.find("年度获奖人")
    #         if index>0:
    #             year=int(a[0:index])
    #             continue
    #         else:
    #             index1=a.find("(")
    #             index2=a.find(")")
    #             name=a[:index1]
    #             birth=a[index1+1:index2]
    #             desc=a[index2+1:]
    #             isT=0
    #             if desc.find("清华")>0 and year>2012:
    #                 isT=1
    #             file.write(str(year)+","+name+","+birth+","+desc+","+str(isT)+'\n')

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
