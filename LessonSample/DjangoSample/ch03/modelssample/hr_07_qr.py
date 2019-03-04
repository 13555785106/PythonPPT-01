#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

print ''.join(['-' for i in xrange(128)])
print '部门id为60的雇员：'
qs = Emp.objects.filter(dep=60)
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print 'IT部门的雇员：'
qs = Emp.objects.filter(dep__name='IT')
for item in qs.values():
    print item

print ''.join(['-' for i in xrange(128)])
print 'Shipping部门工作是Stock Manager的雇员：'
qs = Emp.objects.filter(dep__name='Shipping', job__title='Stock Manager')
for item in qs.values():
    print item
