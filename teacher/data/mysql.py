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


    def insertteacherdata_info(self, item):
        sql = "INSERT INTO teacherdata_info VALUES (NULL,%s,%s,%s,%s,%s)"
        params = (item['name'], item['school'], item['instition'], item['url'], item['info'])
        self.cursor.execute(sql, params)
        self.connect.commit()

    def getTeacher(self):
        sql = "SELECT * from teacherdata_info"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def updateTeacher(self,item):
        param=(item['fields'],item['id'])
        sql = "update teacherdata_info set fields=%s where id=%s"
        self.cursor.execute(sql,param)
        self.connect.commit()

