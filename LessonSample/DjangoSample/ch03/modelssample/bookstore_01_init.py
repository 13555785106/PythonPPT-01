#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os
import random
from datetime import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.bookstore import *

Publisher.objects.all().delete()
pub01 = Publisher.objects.create(name='Pub01', num_awards=3172)
pub02 = Publisher.objects.create(name='Pub02', num_awards=897)
pub03 = Publisher.objects.create(name='Pub03', num_awards=5344)
pub04 = Publisher.objects.create(name='Pub04', num_awards=2202)
pub05 = Publisher.objects.create(name='Pub05', num_awards=1090)

Author.objects.all().delete()
a01 = Author.objects.create(name='A01', age=random.randint(30, 80))
a02 = Author.objects.create(name='A02', age=random.randint(30, 80))
a03 = Author.objects.create(name='A03', age=random.randint(30, 80))
a04 = Author.objects.create(name='A04', age=random.randint(30, 80))
a05 = Author.objects.create(name='A05', age=random.randint(30, 80))
a06 = Author.objects.create(name='A06', age=random.randint(30, 80))

Book.objects.all().delete()

b01 = Book.objects.create(name='B01', pages=360, price=87, rating=90, publisher=pub01, pubdate=datetime.now().date())
b01.authors = [a01, a02]
b01.save()
b02 = Book.objects.create(name='B02', pages=420, price=90, rating=92, publisher=pub01, pubdate=datetime.now().date())
b02.authors = [a01, a02]
b02.save()

b03 = Book.objects.create(name='B03', pages=360, price=87, rating=90, publisher=pub02, pubdate=datetime.now().date())
b03.authors = [a03, a04]
b03.save()
b04 = Book.objects.create(name='B04', pages=420, price=90, rating=92, publisher=pub02, pubdate=datetime.now().date())
b04.authors = [a03, a04]
b04.save()

b05 = Book.objects.create(name='B05', pages=355, price=87, rating=90, publisher=pub04, pubdate=datetime.now().date())
b05.authors = [a05]
b05.save()

b06 = Book.objects.create(name='B06', pages=388, price=90, rating=92, publisher=pub05, pubdate=datetime.now().date())
b06.authors = [a06]
b06.save()

Store.objects.all().delete()

s01 = Store.objects.create(name='S01', registered_users=1000)
s01.books = [b01, b02, b05]
s01.save()

s02 = Store.objects.create(name='S02', registered_users=2000)
s02.books = [b03, b04, b06]
s02.save()
