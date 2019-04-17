import pymysql
#1创建数据库连接
db=pymysql.connect(host="localhost",part=3306,user="root",passwd="123456",db="ha",charset="utf8")
#2.创建游标对象
cursor=db.cursor()
#3.利用游标对象cursor 的方法来操作数据库
cursor.execute("insert into sheng values(11,123456,'新疆省');")

#4.提交到数据库commit
db.commit()
#5.关闭游标对象
cursor.close()
#6.关闭数据库连接
db.close()