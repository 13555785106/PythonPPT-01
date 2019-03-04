# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()

from ch03.models import *

""" 关系记录 """

print '[---Blog的Name为Servlet Tutorial的Entry记录---]'
for entry in Blog.objects.get(name='Servlet Tutorial').entry_set.all():
    print entry.blog.name, entry.headline, entry.pub_date

print '[---Author的Name为Abel Tutorial的Entry记录---]'
for entry in Author.objects.get(name='Alan').entries.all():
    print entry.blog.name, entry.headline, entry.pub_date
