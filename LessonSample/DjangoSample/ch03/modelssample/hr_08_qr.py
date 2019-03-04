#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *
from django.db.models import Q

"""
Q对象的用途是进行更复杂条件的查询，并支持&（and）,|（or），~（not）操作符。
"""
print ''.join(['-' for i in xrange(128)])
print '2001年或者2003年入职的雇员：'
qs = Emp.objects.filter(Q(hire_date__year=2001) or Q(hire_date__year=2003)).order_by('hire_date')
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
#注意Q对象必须放在前面，否则会出错！
print '2001年至2003年入职工资小于5000的雇员：'
qs = Emp.objects.filter(Q(hire_date__year__gte=2001) & Q(hire_date__year__lte=2003)
                        , salary__lt=5000, ).order_by('-hire_date')
for item in qs.values():
    print item
