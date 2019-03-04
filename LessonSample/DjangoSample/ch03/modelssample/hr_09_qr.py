#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *
from django.db.models import F

"""
F表达式用来操作数据表中的某列值，它允许Django在未实际链接数据的情况下具有对数据库字段的值的引用，
不用获取对象放在内存中再对字段进行操作，直接执行原生产sql语句操作。
"""

# SELECT "ch03_emp"."id", "ch03_emp"."first_name", "ch03_emp"."last_name", "ch03_emp"."phone_number", "ch03_emp"."hire_date", "ch03_emp"."salary", "ch03_emp"."commission_pct", "ch03_emp"."manager_id", "ch03_emp"."dep_id", "ch03_emp"."job_id" FROM "ch03_emp" WHERE "ch03_emp"."id" = 206;
# UPDATE "ch03_emp" SET "first_name" = 'William', "last_name" = 'Gietz', "phone_number" = '515.123.8181', "hire_date" = '2002-06-07',
# "salary" = '38100.00', "commission_pct" = 0.0, "manager_id" = 205, "dep_id" = 110, "job_id" = 'AC_ACCOUNT' WHERE "ch03_emp"."id" = 206;

emp = Emp.objects.get(pk=206)
print ''.join(['-' for i in xrange(128)])
emp.salary += 100
emp.save()
# UPDATE "ch03_emp" SET "first_name" = 'William', "last_name" = 'Gietz', "phone_number" = '515.123.8181', "hire_date" = '2002-06-07',
# "salary" = ("ch03_emp"."salary" - 100), "commission_pct" = 0.0, "manager_id" = 205, "dep_id" = 110, "job_id" = 'AC_ACCOUNT' WHERE "ch03_emp"."id" = 206;
print ''.join(['-' for i in xrange(128)])
emp.salary = F('salary') - 100
emp.save()
