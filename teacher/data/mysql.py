import pymysql.cursors
import socket
# 连接数据库
class Mysql(object):

    connect =''
    cursor = ''
    isZhu=True
    def __init__(self):
        if self.isZhu:
            ip = socket.gethostbyname(socket.gethostname())[0:-2]+'.1'
        else:
            ip="localhost"
        self.connect=pymysql.Connect(
            host=ip,
            port=3306,
            user='root',
            passwd='123456',
            db='schoollink',
            charset='utf8'
        )
        self.cursor=self.connect.cursor(cursor=pymysql.cursors.DictCursor)

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
        print("sql:" + sql)
        self.exe_sql(sql, params)
    def exe_sql(self,sql,params=None):

        if params is None:
            self.cursor.execute(sql)
        else :
            self.cursor.execute(sql, params)
        self.connect.commit()
    def insertteacherdata_info(self, item):
        sql = "INSERT INTO teacherdata_info VALUES (NULL,%s,%s,%s,%s,%s)"
        params = (item['name'], item['school'], item['instition'], item['url'], item['info'])
        self.cursor.execute(sql, params)
        self.connect.commit()

    def getTeacher(self):
        sql = "SELECT * from teacherdata_info"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def getSchool(self):
        sql = "SELECT id,name,teacher from school_info"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def updateTeacher(self,item):
        param=(item['fields'],item['id'])
        sql = "update teacherdata_info set fields=%s where id=%s"
        self.cursor.execute(sql,param)
        self.connect.commit()

    def insertSchool(self,item):
        param = (
            item['name'] ,
        item['province'] ,
        item['subjection'] ,
        item['school_type'] ,
        item['level'] ,
        item['characteristic'] ,
        str(item['graduate'] ),
        item['xuexin_url'],
        item['url'] ,
        item['abstract'] ,
        item['logo'] ,
        item['english_name'],
        item['establish'] ,
        item['attribute'],
        item['school_motto'] ,
        item['address'],
        item['national_disciplines'],
        item['master_point'],
        item['doctoral_point'] ,
        item['teacher'] ,
        item['info'])
        sql = "insert into  school_info VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,param)
        self.connect.commit()

