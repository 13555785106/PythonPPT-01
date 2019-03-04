#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.bookstore import *
from django.db.models import Count

q = Book.objects.annotate(Count('authors'), Count('store'))
print q[5].authors__count
print q[5].store__count

q = Store.objects.annotate(Count('books__authors'))
print q[0].books__authors__count
print q[1].books__authors__count
