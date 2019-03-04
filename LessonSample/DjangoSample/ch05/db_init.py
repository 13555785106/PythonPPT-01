#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch05.models import *

# 初始化工资等级表
Hobby.objects.all().delete()
hobbies = [Hobby.objects.create(name='足球'), Hobby.objects.create(name='篮球'), Hobby.objects.create(name='排球'), ]

User.objects.all().delete()

#for i in xrange(97):
#    User.objects.create(account="u%02d" % (i,), passwd="p%02d" % (i,), name="n%02d" % (i,))
