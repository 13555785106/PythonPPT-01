#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3

conn = sqlite3.connect('sqlite3.db')
conn.execute("UPDATE emps SET salary = salary + 1")
conn.commit()
rows = conn.execute("SELECT * FROM emps")
print type(rows)
for row in rows:
    print row[1], row[2], row[3], row[4]
conn.close()
