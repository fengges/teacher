import scrapy
from urllib.parse import quote
from urllib.parse import unquote
from urllib import parse
def qs(url):
    parseResult = parse.urlparse(url)
    param_dict = parse.parse_qs(parseResult.query)
    return param_dict
class CnkiSpider(scrapy.Spider):
    name = 'zhuanxian'
    start_urls = ['http://www.baidu.com']
    file=open('teacher/data/清华_重大专项.csv','w',encoding='utf8')

    def __init__(self):
        self.level = {'核心电子器件、高端通用芯片及基础软件':6,"极大规模集成电路制造技术及成套工艺":11,"新一代宽带无线移动通信":25,"高档数控机床与基础制造技术":14,"大型油气田及煤层气开发":7,"大型先进压水堆及高温气冷堆核电站":7,"大型先进压水堆及高温气冷堆核电站":24,"转基因生物新品种培育":58,'重大新药创制':76,'艾滋病和病毒性肝炎等重大传染病防治':29}
    def start_requests(self):
        for k in self.level:
            for i in range(1,self.level[k]+1):
                url=self.getUrl(k,i)
                yield scrapy.Request(url, callback=self.parse)
    def getUrl(self,level,page):
        level = quote(level, 'utf-8')
        url = 'http://www.nstrs.cn/ashx/baogaoliulan.ashx?pageIndex='+str(page)+'&pageSize=10&action=anjihua&jihua=%E5%9B%BD%E5%AE%B6%E7%A7%91%E6%8A%80%E9%87%8D%E5%A4%A7%E4%B8%93%E9%A1%B9&fieldid='+level+'&flag=1'
        return url

    def parse(self, response):
        level=unquote(qs(response.url)['fieldid'][0], 'utf-8')
        ziran= response.xpath('//tr')
        for l in ziran:
            td=l.xpath('./td')
            text=[]
            for t in td:
                text.append(t.xpath('string(.)').extract()[0])
            tmp=','.join(text).replace('等','')
            # self.file.write(tmp + ',' + level + '\n')
            if tmp.find('清华')>=0:
                self.file.write(tmp+','+level+'\n')



