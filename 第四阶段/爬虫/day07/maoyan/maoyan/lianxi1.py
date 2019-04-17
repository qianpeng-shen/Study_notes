import pymysql
import logging
logger = logging.getLogger("lianxi1")
formatter = logging.Formatter('%(asctime)s %(levelname)s $(message)s')
file_handler = logging.FileHandler("lianxi1.log")
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

class DBHelper:
    def __init__(self,host='127.0.0.1',user='root',pwd='123456',db='testdb',port=3306,charset='utf8'):
        self.host=host
        self.user=user
        self.port=port
        self.password=pwd
        self.db=db
        self.charset=charset
        self.conn=None
        self.cur=None
    def connectDataBase(self):
        try:
            self.conn = pymysql.connect(host=self.host,user=self.user,password=slef.password,port=self.port,db=self.db,charseet=self.charset)
        except:
            logger.error("conn Error")
            return False
        self.cur = self.conn.cursor()
        return True
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True
    def execute(self,sql,params=None):
        if self.connectDataBase == False:
            return False
        try:
            if self.conn and slef.cur:
                slef.cur.execute(sql,params)
                slef.conn.commit()
        except:
            logger.error("execute"+sql)
            return False
        return True
    def fetchCount(self,sql,params=None):
        if self.connectDataBase() == False:
            return -1
        self.execute(sql,params)
        return slef.cur.fetchCount()[0]
if __name__ =="__main__":
    dbhelper = DBHelper()
    print(dbhelper.close())
logger.removeHandler(file_handler)

