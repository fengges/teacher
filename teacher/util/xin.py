
import re

from teacher.data.readName import *

class Xin(object):
    xin=[]
    filt=['宋体','党校在线','查看详情>','后流动站','查看更多+','查看简历','简体中文','-','任职','查看详情','@','党员发展','党风廉政','后台登陆','文章列表','国家基地','关工委','成人教育','广延名师','国家千人','有关表格','文件资料','博士后','党务','祝福','经典','家园','项目','幸福','博士后','毕业','交流','国内','党委','风采','班团','培训','平台','汇总','高峰','计划','荣誉','奖励','包括','方法','高等','教育学','高职','科学','党代会','党政','党团','后勤服务','支部','工作','全文','关闭','通讯','高级','党建','尚无','有用','应用','计算','相关','公共','成果','师资','全职','教师','顾问','海外','通知','公告','管理','毕业生','国际','马上','高端','全部','论文','计算机','学院','常用','下载','党群','组织','成就','关于','法治','法制']
    rep=['\xa0','[',']','(',')','（','）',':','：',' ',' ','.',',','/','*','、','，',"教师风采","博后","特任研究员","研究员",'☆','简讯','讲师','副教授','教授','客座','讲座','博士生导师','硕士生导师','硕士','导师','博士','姓名','双聘','主任','简介','师资概况','团队','名录','高工','兼聘','院士','兼职','申请','年至','年出生','入选','书院']
    def __init__(self):
        file="teacher/data/name.txt"
        file2 = "name.txt"
        try:
            self.xin=readXin(file)
        except:
            self.xin = readXin(file2)
    def findXin(self,name):
        for x in self.xin:
            try:
                index=name.index(x)
                if index==0:    #姓要出现在第一个
                    return 1
            except:
                pass
        return 0
    def reName(self,name):
        if name is None:
            print("None")
            return 1
        p1 = re.compile('\s+')
        # p2=re.compile('[a - zA - Z0 - 9]+')
        # info = re.sub(p2, " ",info)
        name = re.sub(p1, ' ', name)
        for r in self.rep:
            name = name.replace(r, ' ')
        return name
    def isXin(self,name):
        if name is None:
            print("None")
            return 0
        p1 = re.compile('\s+')
        # p2=re.compile('[a - zA - Z0 - 9]+')
        # info = re.sub(p2, " ",info)
        name = re.sub(p1, ' ', name)
        for r in self.rep:
            name=name.replace(r,'')
        name=re.sub('[a-zA-Z]+', '', name)
        for n in self.filt: #判断名字是否在过滤表上
            index = name.find(n)
            if index>=0:
                return 0
        l=len(name)
        if(l<2):     # 判断名字是否符合长度
            return 0
        if(l>5):
            return 0
        return self.findXin(name)

    def getXin(self,name):
        if name is None:
            print("None")
            return ""
        p1 = re.compile('\s+')
        # p2=re.compile('[a - zA - Z0 - 9]+')
        # info = re.sub(p2, " ",info)
        name = re.sub(p1, ' ', name)
        for r in self.rep:
            name=name.replace(r,'')
        name=re.sub('[a-zA-Z]+', '', name)
        for n in self.filt: #判断名字是否在过滤表上
            index = name.find(n)
            if index>=0:
                return ""
        l=len(name)
        if(l<2):     # 判断名字是否符合长度
            return ""
        if(l>5):
            return ""
        if self.findXin(name)==1:
            return name

    def get(self,name):
        if name is None:
            print("None")
            return ""
        p1 = re.compile('\s+')
        # p2=re.compile('[a - zA - Z0 - 9]+')
        # info = re.sub(p2, " ",info)
        name = re.sub(p1, ' ', name)
        for r in self.rep:
            name=name.replace(r,'')
        name=re.sub('[a-zA-Z]+', '', name)
        for n in self.filt: #判断名字是否在过滤表上
            index = name.find(n)
            if index>=0:
                return ""

        return name