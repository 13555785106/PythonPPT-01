# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()

from ch03.models import *

""" 使用filter及exclude筛选对象 """
# filter 包含指定条件的记录
# exclude 排除指定条件的记录
print '[---2017年但是不包含2月的记录---]'
for entry in Entry.objects.filter(pub_date__year=2017).exclude(pub_date__month=2):
    print entry.headline, entry.pub_date
print '[---大于等于2017-3-1小于等于2017-8-31的记录---]'
for entry in Entry.objects.filter(pub_date__lte='2017-8-31', pub_date__gte='2017-3-1'):
    print entry.headline, entry.pub_date

print '[---2017与2018年的记录---]'
for entry in Entry.objects.filter(pub_date__year__lte=2018, pub_date__year__gte=2017):
    print entry.headline, entry.pub_date

"""
字段查询关键字参数
exact
iexact
contains
icontains
in
gt
gte
lt
lte
startswith
istartswith
endswith
iendswith
range
date
year
month
day
week
week_day
time
hour
minute
second
isnull
search
regex
iregex
"""
