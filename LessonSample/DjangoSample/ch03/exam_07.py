# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.models import *
from django.db.models import F

""" 
修改
"""

entry = Entry.objects.get(pk=151)
entry.click_count += 1
entry.save()

Entry.objects.filter(pub_date__month=3).update(click_count=100)
# F 表达式
Entry.objects.filter(pub_date__month__gte=2, pub_date__month__lte=3).update(click_count=F('click_count') + 10)
