# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.models import *

""" 惰性加载 """

result = Entry.objects.values('blog__id').distinct()

# 执行查询
print result
# 还是要执行查询
print result.count()
print '>-----------------------------------<'
# 查询缓存结果
result = [v for v in Entry.objects.values('blog__id').distinct()]
print result
print len(result)
