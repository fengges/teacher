import scrapy
from urllib.parse import quote
from urllib.parse import unquote
from urllib import parse
def qs(url):
    parseResult = parse.urlparse(url)
    param_dict = parse.parse_qs(parseResult.query)
    return param_dict

class CnkiSpider(scrapy.Spider):
    name = 'ziranjijin'
    start_urls = ['http://www.baidu.com']

    def __init__(self):
        self.file = open('teacher/data/清华_自然基金.csv', 'w', encoding='utf8')
    def start_requests(self):
        teacher=open('teacher/data/清华名单.txt','r',encoding='utf8').readlines()[1:]
        self.file.write('姓名,批准号,负责人,项目,是否是负责人\n')
        for t in teacher:
            t=t.replace('\n','')
            name=t
            name= quote(name, 'utf-8')
            url1='https://isisn.nsfc.gov.cn/egrantindex/funcindex/viewPubProjectDeatil?orgId=QXT5%2F1DY6%2BfoSqaw4ZATTFJllFVvuiM%2B&psnName='+name+'&orgName=%25E6%25B8%2585%25E5%258D%258E%25E5%25A4%25A7%25E5%25AD%25A6&isPc=1'
            yield scrapy.FormRequest(
                url=url1,
                formdata={
                     'nd': '1537881720345',#这里不能给int类型的1，requests模块中可以
                    '_search':'false',
                    'rows':'100',
                    'page':'1'
                },
                callback=self.parse
            )
            url2='https://isisn.nsfc.gov.cn/egrantindex/funcindex/viewPubProjectDeatil?orgId=QXT5%2F1DY6%2BfoSqaw4ZATTFJllFVvuiM%2B&psnName='+name+'&orgName=%25E6%25B8%2585%25E5%258D%258E%25E5%25A4%25A7%25E5%25AD%25A6&isPc=0'
            yield scrapy.FormRequest(
                url=url2,
                formdata={
                     'nd': '1537881720345',#这里不能给int类型的1，requests模块中可以
                    '_search':'false',
                    'rows':'100',
                    'page':'1'
                },
                callback=self.parse
            )
    def parse(self, response):
        isPc=qs(response.url)['isPc'][0]
        name=unquote(qs(response.url)['psnName'][0], 'utf-8')
        teacher= response.xpath('//row')
        for t in teacher:
            item={}
            item['id']=t.xpath('./cell[1]/text()').extract()[0]
            item['pc_name']=t.xpath('./cell[2]/text()').extract()[0]
            item['project'] = t.xpath('./cell[4]/text()').extract()[0]
            print(item)
            if int(isPc)==1:
                self.file.write(name+','+item['id']+','+item['pc_name']+','+item['project']+',是\n')
            else:
                self.file.write(name + ',' + item['id'] + ',' + item['pc_name'] + ',' + item['project'] + ',不是\n')

