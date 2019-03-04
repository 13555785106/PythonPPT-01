#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os
from datetime import datetime

import django
import xlrd

"""
读取hr-exam.xls文件，对hr相关的表进行初始化。
"""

# 获取 hr-exam.xls 文件全路径
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hr-exam.xls')
# 读取excel文件中的雇员数据并保存到数据库中
wb = xlrd.open_workbook(filename)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

# 初始化工资等级表
SalGrade.objects.all().delete()
sheet = wb.sheet_by_name('salgrade')
for rowNum in xrange(sheet.nrows):
    if rowNum >= 1:
        sal_grade = SalGrade.objects.create(
            level=sheet.cell(rowNum, 0).value,
            min_salary=sheet.cell(rowNum, 1).value,
            max_salary=sheet.cell(rowNum, 2).value)

qs = SalGrade.objects.all()
print ''.join(['-' for i in xrange(128)])
print '***【工资等级表】 总计 %d 条记录 ***' % qs.count()
print ''.join(['-' for i in xrange(128)])
for item in qs.values():
    print item
print ''.join(['-' for i in xrange(128)])
print
print
print

# 初始化部门表
Dep.objects.all().delete()
sheet = wb.sheet_by_name('dep')
for rowNum in xrange(sheet.nrows):
    if rowNum >= 1:
        dep = Dep.objects.create(
            id=sheet.cell(rowNum, 0).value,
            name=sheet.cell(rowNum, 1).value)

qs = Dep.objects.all()
print ''.join(['-' for i in xrange(128)])
print '***【部门表】 总计 %d 条记录 ***' % qs.count()
print ''.join(['-' for i in xrange(128)])
for item in qs.values():
    print item
print ''.join(['-' for i in xrange(128)])
print
print
print

# 初始化工作表
Job.objects.all().delete()
sheet = wb.sheet_by_name('job')
for rowNum in xrange(sheet.nrows):
    if rowNum >= 1:
        job = Job.objects.create(
            id=sheet.cell(rowNum, 0).value,
            title=sheet.cell(rowNum, 1).value,
            min_salary=sheet.cell(rowNum, 2).value,
            max_salary=sheet.cell(rowNum, 3).value)

qs = Job.objects.all()
print ''.join(['-' for i in xrange(128)])
print '***【工作表】 总计 %d 条记录 ***' % qs.count()
print ''.join(['-' for i in xrange(128)])
for item in qs.values():
    print item
print ''.join(['-' for i in xrange(128)])
print
print
print

# 雇员表
Emp.objects.all().delete()
sheet = wb.sheet_by_name('emp')
for rowNum in xrange(sheet.nrows):
    if rowNum >= 1:
        emp = Emp()
        emp.id = sheet.cell(rowNum, 0).value
        emp.first_name = sheet.cell(rowNum, 1).value
        emp.last_name = sheet.cell(rowNum, 2).value
        emp.phone_number = sheet.cell(rowNum, 4).value
        emp.hire_date = datetime.strptime(sheet.cell(rowNum, 5).value, '%Y-%m-%d')
        emp.salary = sheet.cell(rowNum, 7).value
        emp.commission_pct = sheet.cell(rowNum, 8).value
        emp.manager_id = sheet.cell(rowNum, 9).value
        try:
            emp.dep = Dep.objects.get(pk=sheet.cell(rowNum, 10).value)
        except Dep.DoesNotExist:
            pass
        emp.job = Job.objects.get(pk=sheet.cell(rowNum, 6).value)
        emp.save()

qs = Emp.objects.all()
print ''.join(['-' for i in xrange(128)])
print '***【雇员表】 总计 %d 条记录 ***' % qs.count()
print ''.join(['-' for i in xrange(128)])
for item in qs.values():
    print item
print ''.join(['-' for i in xrange(128)])
