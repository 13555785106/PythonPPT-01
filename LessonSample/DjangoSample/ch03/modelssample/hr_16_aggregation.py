#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *
from django.db.models import Avg, Max, Min,Sum, DecimalField, Count

"""
聚合函数
    相当于SQL中的聚合函数，对一组值执行计算，并返回单个值。
    aggregate()是用于整个QuerySet对象的汇总值 。
    而annotate()函数可以为QuerySet中的每个对象生成一个独立的摘要，
    输出的结果仍然是一个QuerySet对象，能够调用filter()、order_by()甚至annotate()
"""

print Emp.objects.all().aggregate(Max('salary'))  # 值是Decimal类型
print Emp.objects.all().aggregate(Min('salary'))  # 值是Decimal类型
print Emp.objects.all().aggregate(Sum('salary'))
print Emp.objects.all().aggregate(emp_salary_avg=Avg('salary'))  # 值是float类型
print Emp.objects.all().aggregate(Max('salary'), Min('salary'), Avg('salary'), Count('id'))

# all()函数加与不加都可！
print Emp.objects.aggregate(
    salary_diff=Max('salary', output_field=DecimalField()) - Avg('salary', output_field=DecimalField()))

deps = Dep.objects.annotate(Count('emp')).order_by('-emp__count')
print '%-20s%-9s' % ('DEP_NAME', 'NUM_EMPS')
for dep in deps:
    print '%-20s%-9s' % (dep.name, dep.emp__count)

deps = Dep.objects.annotate(num_emps=Count('emp')).order_by('-num_emps')
print '%-20s%-9s' % ('DEP_NAME', 'NUM_EMPS')
for dep in deps:
    print '%-20s%-9s' % (dep.name, dep.num_emps)

