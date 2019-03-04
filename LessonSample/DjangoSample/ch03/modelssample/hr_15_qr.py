#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

"""
一对多关系结果显示
"""

# deps = Dep.objects.all()
# deps = Dep.objects.select_related().all()
# for dep in deps:
#     empList = [emp for emp in dep.emp_set.all()]
#     if empList:
#         print '部门: %s' % dep.name
#         print empList

dep = Dep.objects.get(pk=100)
print dep
emps = Emp.objects.filter(pk__gte=200)

dep.emp_set.add(*[emp for emp in emps])

print dep.emp_set.count()
"""
add(obj1, obj2, ...)    为指定模型添加关系对象
create(**kwargs)        为指定模型创建一个关系对象
remove(obj1, obj2, ...) 移除
clear()                 全部清除
set(objs)               替换
"""
