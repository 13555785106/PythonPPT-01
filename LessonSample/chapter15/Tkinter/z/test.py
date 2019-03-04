#!/usr/bin/python
# -*- coding: UTF-8 -*-
a, b, c = 1, 2, 3
print '.upper()' if 1 != 1 else '.title()'
print [v for v in xrange(10)]
print [b, a][a > b]
print (a>b and a or b)
print (a>b and [a] or [b])[0]

import cx_Oracle

conn = cx_Oracle.connect('hr/123456@localhost/xe')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
curs = conn.cursor()
sql = 'select * from employees'  # sql语句
rr = curs.execute(sql)
row = curs.fetchone()
print(row)
curs.close()
conn.close()
