#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

"""
使用对象的Manager可以从数据库获取QuerySet。
QuerySet代表了数据库对象的集合，它可以使用过滤器来限制结果的数量。
从SQL角度来说，QuerySet相当于SELECT，过滤器相当于 WHERE或者LIMIT
"""
qs = Emp.objects.all()
# print type(qs)
# for v in dir(qs):
#     print v

print "雇员总数为 %s" % qs.count()
for item in qs:
    print item  # 元素为 Emp对象

# for item in qs.values():
#     print item  # 元素为 字典对象
#
# for item in qs.values_list():
#     print item  # 元素为 元组对象
