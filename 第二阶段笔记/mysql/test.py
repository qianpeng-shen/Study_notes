from ddd import mysqlpython

sqlh=mysqlpython("localhost",3306,"ha","root","123456")
sql_update="update sheng set id=150 where id=1;"
sqlh.zhixing(sql_update)