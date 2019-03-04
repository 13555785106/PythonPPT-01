#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *
from django.db import connection

"""
raw SQL
"""

for emp in Emp.objects.raw('SELECT * FROM ch03_emp'):
    print(emp)
"""传递参数"""
for emp in Emp.objects.raw("SELECT * FROM ch03_emp WHERE last_name = %s", ['King']):
    print(emp)

"""直接通过游标操作数据库"""
c = connection.cursor()
try:
    c.execute("SELECT * FROM ch03_emp")
    for row in c.fetchall():
        print row
finally:
    c.close()
