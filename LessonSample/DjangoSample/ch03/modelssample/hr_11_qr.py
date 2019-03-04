#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *

"""
对结果集进行缓存以提高运行效率
"""

# 结果集不会被缓存，以下使用方式，每次取第一条记录都会导致一次查询！！！！！！
qs = Emp.objects.all()
print qs[0]
print qs[0]

# 正确的使用方式
qs_list = [v for v in Emp.objects.all()]
print qs_list[0]
print qs_list[0]
