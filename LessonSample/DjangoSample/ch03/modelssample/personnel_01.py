#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os
from datetime import datetime, date

# api文档 https://docs.djangoproject.com/en/1.7/ref/models/querysets/
import django

# from django.db.modelssample import Sum,Avg,Count,Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()

from ch03.modelssample.personnel import Person, Group, Membership

Person.objects.all().delete()
Group.objects.all().delete()

p1 = Person.objects.create(first_name="大力", last_name='王', shirt_size='M', birthday=date(1972, 1, 1), salary=9999999.99)
p2 = Person.objects.create(first_name="俊峰", last_name='肖', shirt_size='L', birthday=date(1973, 1, 1))
g1 = Group.objects.create(name="Python组")
m1 = Membership(person=p1, group=g1,
                date_joined=datetime.now().date(),
                invite_reason="工作太多了")
m1.save()
print g1.members.all()
print p1.group_set.all()

m2 = Membership.objects.create(person=p2, group=g1,
                               date_joined=datetime.now().date(),
                               invite_reason="人手不够了")
print g1.members.all()
