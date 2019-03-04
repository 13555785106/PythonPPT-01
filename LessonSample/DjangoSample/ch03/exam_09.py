# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.models import *
from django.db.models import *

""" values 函数及以某列分组聚合 """
# values 函数可以指定输出结果包含的字段，以字典形式返回
#
result = Entry.objects.values('headline', 'click_count')

for v in result:
    print v['headline'], v['click_count']

# 以 headline 进行分组
# 此时以 values 函数中指定的列进行分组
print '>-----------------------------------<'
result = Entry.objects.values('headline').annotate(click_count=Sum('click_count'))
for v in result:
    print v
