#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3

create_emps_sql = """
CREATE TABLE IF NOT EXISTS EMPS(
ID INTEGER PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INTEGER NOT NULL,
ADDRESS TEXT,
SALARY REAL CHECK(SALARY > 0) 
)"""


conn = sqlite3.connect('sqlite3.db')
cursor = conn.cursor()
cursor.execute(create_emps_sql)
conn.commit()
conn.close()
