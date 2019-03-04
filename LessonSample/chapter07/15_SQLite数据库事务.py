#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3

conn = sqlite3.connect('sqlite3.db')

try:
    conn.execute("UPDATE emps SET salary=salary+1000 WHERE id = ?", (1,))
    conn.execute("UPDATE emps SET salary=salary-1000 WHERE id = ?", (2,))
    conn.commit()
except Exception, e:
    print e
    conn.rollback()

# conn.commit()

rows = conn.execute("SELECT * FROM emps")

for row in rows:
    print '%d,%s,%d,%s,%.2f' % row

conn.close()
