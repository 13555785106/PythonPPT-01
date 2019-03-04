#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os
from datetime import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

"""
创建、修改、删除对象。
"""
# 通过构造函数创建对象，必须save才能保存到数据库。
# 如果对象已经存在，会进行更新。
dep = Dep(id=1000, name='开发部A')  # 创建
dep.save()  # 保存
print Dep.objects.get(id=1000)
dep = Dep(id=1000, name='开发部B')
dep.save()
print Dep.objects.get(id=1000)
dep.delete()  # 删除

# 通过管理器的create创建对象，不需要保存。
# 如果对象已经存在，创建会失败！
dep = Dep.objects.create(id=1001, name='销售部')  # 创建
print Dep.objects.get(id=1001)
Dep.objects.get(id=1001).delete()  # 删除

# 创建带存在外键的对象

emp = Emp()
emp.id = 10000
emp.first_name = '俊峰'
emp.last_name = '肖'
emp.phone_number = '13555785106'
emp.hire_date = datetime.now().date()
emp.salary = 20000.90
emp.commission_pct = 0.99
emp.manager_id = 100
emp.dep = Dep.objects.get(pk=10)
emp.job = Job.objects.get(pk='AD_PRES')
emp.save()

print Emp.objects.get(id=10000)
Emp.objects.get(id=10000).delete()  # 删除

# 将id=206的雇员工资改为38000
emp = Emp.objects.get(id=206)
emp.salary = 38000
emp.save()

emp = Emp.objects.get(id=206)
print emp.salary
