import pymysql.cursors
import socket
# 连接数据库
class Mysql(object):

    connect =''
    cursor = ''
    isZhu=True
    def __init__(self):

        ip="47.104.236.183"
        self.connect=pymysql.Connect(
        host=ip,
        port=3306,
        user='root',
        passwd='SLX..eds123',
        db='eds',
        charset='utf8'
)
        self.cursor=self.connect.cursor()
# 获取游标

    # cursor=''
    # school操作
    def insertItem(self, item):
        # insert into student_info(stuName,stuAge) values('liutao',13)
        table = item["table"] + "("
        temp = ",".join(["%s" for i in item["params"]])
        column = " values(" + temp + ")"
        paramList = []
        columnList = []
        for k in item["params"]:
            columnList.append(k)
            paramList.append(item["params"][k])
        params = tuple(paramList)
        sql = "insert into " + table + ",".join(columnList) + ")" + column
        self.exe_sql(sql, params)
    def getSchoolByName(self,name):
        sql = "SELECT * FROM school_info where name like %s"
        params = ("%"+name+"%",)
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    def updateByName(self,name,item):
        sql = "update  school_info set title=%s,star=%s,scope=%s where name like %s"
        params = (item["title"],item["star"],item["scope"],"%"+name+"%")
        self.cursor.execute(sql, params)
        self.connect.commit()
    #获取
    def getSchool(self,search):
        sql = "SELECT * FROM `eds_985institution_teacherlist` where flag=%s"
        self.cursor.execute(sql,(search))
        return self.cursor.fetchall()
    def updateSchoolbyUrl(self,url,search):
        sql="update `eds_985institution_teacherlist` set flag=%s where institution_url=%s"
        params=(search,url)
        self.cursor.execute(sql, params)
        self.connect.commit()
    #更新
    def updateSchool(self,id,search):
        sql="update `eds_985institution_teacherlist` set flag=%s where id=%s"
        params=(search,id)
        self.cursor.execute(sql, params)
        self.connect.commit()

    #插入
    def insertSchool(self,item):

        sql="INSERT INTO school VALUES (NULL,%s,%s,%s,0) "
        params=(item['school'],item['adpart'],item['url'])
        self.cursor.execute(sql,params)
        self.connect.commit()

    def insertSchool2(self,item):

        sql="INSERT INTO school VALUES (NULL,%s,%s,%s,100) "
        params=(item['school'],item['adpart'],item['url'])
        self.cursor.execute(sql,params)
        self.connect.commit()

    def insertteacherdata_info(self, item):
        sql = "INSERT INTO teacherdata_info VALUES (NULL,%s,%s,%s,%s,%s)"
        params = (item['name'], item['school'], item['instition'],item['url'],item['info'])
        self.cursor.execute(sql, params)
        self.connect.commit()
    def getTeacher(self):
        sql = "SELECT * from teacherData2 where search=0 or search>=10 limit 500,100"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getAllTeacher(self):
        sql = "SELECT * from teacherData2"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getAllTeacher3(self):
        sql = "SELECT * from teacher"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getAllTeacher2(self):
        sql = "SELECT * from teacher2"
        self.cursor.execute(sql)

        return self.cursor.fetchall()
    def deleteTeacher(self,id):
        sql = "delete from teacher2 where id=%s"
        self.cursor.execute(sql,(id))
        self.connect.commit()

    def TeacherupdateHtml(self,item):
        sql = "update teacherData2 set info=%s,original_html=%s,image=%s,search=1 where id=%s"
        params = (item['info'],item['original_html'],item['image'],item['id'])
        self.cursor.execute(sql, params)
        self.connect.commit()

    def updateTeacherUrl(self,link,id):
        sql="update teacherData2 set link=%s, search=1 where id=%s"
        params=(link,id)
        self.cursor.execute(sql,params)
        self.connect.commit()

    def insertTeacherLink(self,item):
        sql="insert into teacherData2 values(NULL,%s,%s,%s,%s,%s,%s,NUll,NUll,NUll,0)"
        params=(item['name'],item['link'],item['all_link'],item['school'],item['institution'],item['institution_url'])
        self.cursor.execute(sql,params)
        self.connect.commit()

    def select(self):
        # sql="SELECT count(name) as sum,link,institution_url FROM `teacherdata2` GROUP BY link,institution_url having sum>1"
        sql='SELECT count(*) as sum, id_paper_left,id_paper_right  FROM `paper_dot` GROUP BY id_paper_left,id_paper_right HAVING sum>1'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def updateT(self,item):
        sql = "update teacher2 set institution_url=%s , all_link=%s , school=%s ,issplit=1 where id=%s"
        params = (item['institution_url'], item['all_link'],item['school'],item['id'])
        self.cursor.execute(sql,params)
        self.connect.commit()
    def selectall(self):
        sql="SELECT * FROM `teacherdata2`"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def selectItem(self,item):
        # sql="SELECT id,name,link  FROM `teacherdata2` where  link=%s and institution_url=%s"
        sql='SELECT * FROM `paper_dot` where id_paper_left=%s and id_paper_right=%s'
        params = (item['id_paper_left'], item['id_paper_right'])
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def delItem(self, id):
        sql = "delete from `teacherdata2` where id="+str(id)
        self.cursor.execute(sql)
        self.connect.commit()

    def getAbstracts(self):
        sql="select id,abstract from paper where abstract!=''"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_paper_length(self,item):
        sql="insert into paper_length value(NULL,%s,%s,%s,1,NULL)"
        params = (item['id'],item['vertor'], item['dot'])
        self.cursor.execute(sql, params)
        self.connect.commit()

    def insert_paper_dot(self,item):
        sql="insert into paper_dot values(NULL,%s,%s,%s,1)"
        params = (item['id_paper_left'],item['id_paper_right'], item['value'])
        self.cursor.execute(sql, params)
        self.connect.commit()

    def insert_paper_dot_many(self, item):
        self.cursor.executemany("insert into paper_dot values(NUll,%s,%s,%s,1)",item)
        self.connect.commit()

    def exe_sql(self,sql,params=None):
        if params is None:
            self.cursor.execute(sql)
        else :
            self.cursor.execute(sql, params)
        self.connect.commit()

    def get_sql(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insertTeacher(self, item):
        sql = "insert into teacher values(NULL,%s,null,null,%s,%s,null,NUll,NUll,null,%s)"
        params = (item['name'], item['school'], item['institution'], item['all_link'])
        self.cursor.execute(sql, params)
        self.connect.commit()
    def get_url_num(self,item):
        sql='select count(*) as num from teacher2 where all_link=%s'
        params = (item)
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    def get_teacher(self,item):
        sql='select * from teacher2 where institution=%s and school=%s and name=%s and all_link=%s'
        params = (item['institution'], item['school'], item['name'],item['all_link'])
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    def get_teacher2(self,item):
        sql='select * from teacher2 where school=%s and name=%s and institution=%s'
        params = (item['school'], item['name'],item['institution'])
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def getPaperId(self):
        sql='SELECT paper_id FROM `paper_length` where paper_id not in(SELECT id_paper_left FROM `paper_dot` GROUP BY id_paper_left) ;'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def getPaperUrl(self,ids):
        sql='SELECT url FROM `paper` where id in '+ids
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getMeetId(self):
        sql = 'SELECT id,recommend FROM cr_competition '
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getMeetById(self,id):
        sql = 'SELECT id FROM cr_meeting where id='+id
        self.cursor.execute(sql)
        return self.cursor.fetchall()