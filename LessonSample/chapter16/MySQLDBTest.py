#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector

# 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
con = mysql.connector.connect(
    host='192.168.3.9', port=3306,
    user='exam', passwd='123456',
    database='exam', use_unicode=True)

# 使用cursor()方法获取操作游标
cursor = con.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print "Database version : %s " % data
cursor.close()
con.close()

