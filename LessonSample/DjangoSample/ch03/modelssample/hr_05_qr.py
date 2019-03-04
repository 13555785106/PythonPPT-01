#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

print ''.join(['-' for i in xrange(128)])
print '2003年入职的雇员：'
qs1 = Emp.objects.filter(hire_date__year=2003)
for item in qs1.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '2003年5月入职的雇员：'
qs2 = qs1.filter(hire_date__month=5)
for item in qs2.values():
    print item

print ''.join(['-' for i in xrange(128)])
print '2003年5月1日入职的雇员：'
qs3 = qs2.filter(hire_date__day=1)
for item in qs3.values():
    print item
