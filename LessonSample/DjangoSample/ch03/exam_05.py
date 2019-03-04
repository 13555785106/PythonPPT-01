# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()

from ch03.models import *

""" 关系查询 """

print '[---Blog的Name为Servlet Tutorial的记录---]'
for entry in Entry.objects.filter(blog__name='Servlet Tutorial'):
    print entry.blog.name, entry.headline, entry.pub_date

print '[---Author的Name为Abel的记录---]'
for entry in Entry.objects.filter(authors__name='Abel'):
    print entry.authors.all(), entry.headline, entry.pub_date

print '[---Author的Name为Abel的Blog---]'
for blog in Blog.objects.filter(entry__authors__name='Alan'):
    print blog
