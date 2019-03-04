#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *
from django.db.models import F
"""
删除结果集
"""

#Emp.objects.get(pk=206).delete()
print Emp.objects.filter(pk=206).delete()
print Emp.objects.filter(hire_date__year=2002).delete()
