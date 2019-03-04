# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.models import *
from django.db.models import *

""" 聚合 """
print '*------------------------------------*'
print Entry.objects.aggregate(Avg('click_count'), Count('click_count'), Sum('click_count'), Min('click_count'),
                              Max('click_count'))
print '*------------------------------------*'
print Entry.objects.aggregate(Count('headline', distinct=True))

# annotate 会以当前模型的所有字段作为分组条件
print '*------------------------------------*'
print Blog.objects.annotate(number_of_entries=Count('entry'))
print '*------------------------------------*'
for v in Author.objects.annotate(number_of_blogs=Count('entries__blog', distinct=True)):
    print v, v.number_of_blogs
