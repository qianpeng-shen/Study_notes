import pymysql
import re
f=open('zidian.py')
db=pymysql.connect('localhost','root','123456','dict',charset='utf8')
cur=db.cursor()
for lien in f:
    l=re.split('[ ]+',lien)
    sql="insert into words (word,interpret) values('%s','%s')"%(l[0],' '.join(l[1:]))
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()

