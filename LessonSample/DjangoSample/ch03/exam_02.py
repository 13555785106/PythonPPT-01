# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.models import *
print '通过all函数获取所有对象'
for author in Author.objects.all():
    print author
print '按名称降序排序'
for author in Author.objects.order_by('-name'):
    print author

print '通过主键获取单一对象'
# 通过get方法获取对象只能是一条记录，无记录或者多于一条都会抛出异常
print Author.objects.get(pk=322)
print Author.objects.get(id=322)
