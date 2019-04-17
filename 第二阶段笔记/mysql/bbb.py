import pymysql

db=pymysql.connect("localhost","root","123456",
    "ha",charset="utf8")

cur = db.cursor()
# sql_select = "select * from city"
cur.execute("select * from city;")
data=cur.fetchone()
print("fetchone的结果为:",data)
data2=cur.fetchmany(2)
print("fetchone的结果为:")
for i in data2:
    print(i)
data3=cur.fetchall()
print("fetchall的结果为:")
for x in data3:
    print(x)

db.commit()
cur.close()
db.close()