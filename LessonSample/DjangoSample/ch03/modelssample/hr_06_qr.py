#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

print ''.join(['-' for i in xrange(128)])
print '2005年入职工资降序入职日期降序的雇员：'
qs = Emp.objects.filter(hire_date__year=2005).order_by('-salary', '-hire_date')  # 排序使用属性名，前面加个-号，表示降序
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '2005年入职工资降序排序后前5名：'
qs = Emp.objects.filter(hire_date__year=2005).order_by('-salary')[:5]  # 排序使用属性名，前面加个-号，表示降序
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '2005年入职工资降序排序后前5名：'
qs = Emp.objects.all()[:10:3]
for item in qs:
    print item
