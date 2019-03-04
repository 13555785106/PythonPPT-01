#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3

# 使用 ？ 占位符
insert_emp_sql_01 = """
INSERT INTO EMPS (NAME,AGE,ADDRESS,SALARY)
VALUES (?,?,?,?)"""
# 使用命名占位符
insert_emp_sql_02 = """
INSERT INTO EMPS (NAME,AGE,ADDRESS,SALARY)
VALUES (:name,:age,:address,:salary)"""

conn = sqlite3.connect('sqlite3.db')

conn.execute("DELETE FROM emps")
conn.execute(insert_emp_sql_01,('Tom', 36, u'沈阳市', 2000))
conn.execute(insert_emp_sql_02,
               {'name': 'John', 'age': 28, 'address': u'长沙市', 'salary': 2000})

conn.executemany(insert_emp_sql_01,
                   [[unicode(u"琼斯" + str(i)), 10 + i, unicode(u"沈阳市" + str(i)), 200 + i] for i in xrange(30)])
conn.commit()


conn.close()
