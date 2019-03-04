#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import mysql.connector

conn = mysql.connector.connect(
    user='test',
    password='123456',
    database='test',
    use_unicode=True)
cursor = conn.cursor()
for i in range(30):
    cursor.execute('insert into students (name) values (%s)', ['Michael'+str(i)])
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from students')
for v in cursor.fetchall():
    print v[0],v[1]
cursor.close()
conn.close()