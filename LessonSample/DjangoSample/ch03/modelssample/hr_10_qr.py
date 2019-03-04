#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

"""
通过主键获取对象
"""

print Emp.objects.get(pk=206)  # 如果没有对应的记录，会抛出DoesNotExist异常
print Emp.objects.get(id=206)  # 如果没有对应的记录，会抛出DoesNotExist异常

print Emp.objects.filter(pk=206)  # 如果没有对应的记录，不会抛出异常
print Emp.objects.filter(id=206)  # 如果没有对应的记录，不会抛出异常

print Emp.objects.filter(id__in=(204, 205, 206))
