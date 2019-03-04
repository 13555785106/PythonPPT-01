# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from django.db.models import Q
from ch03.models import *

""" 
使用Q对象设置复杂查询条件 
&   与 
|   或
~   非,即取反
"""

print '------------------------------------'
for author in Author.objects.filter(Q(name__startswith='A') & Q(email__endswith='163.com')):
    print author.name, author.email

print '------------------------------------'
for author in Author.objects.filter(~Q(name__startswith='A') & ~Q(email__endswith='163.com')):
    print author.name, author.email
