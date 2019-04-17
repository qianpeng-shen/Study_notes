import pymysql
db=pymysql.connect("localhost","root","123456","ha",charset="utf8")
cur=db.cursor()
cur.execute("select * from city")
data=cur.fetchone()
print("结果为:",data)
db.commit()
cur.close()
db.close()
