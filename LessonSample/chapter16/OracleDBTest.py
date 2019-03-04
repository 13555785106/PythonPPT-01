#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cx_Oracle

# 用自己的实际数据库用户名、密码、主机ip地址 替换即可
conn = cx_Oracle.connect('hr/123456@192.168.3.44/orcl')
cursor = conn.cursor()
sql = 'select * from employees'  # sql语句
cursor.execute(sql)
results = cursor.fetchall()
print cursor.rowcount
print dir(results)
for row in results:
    print row
cursor.close()
conn.close()
