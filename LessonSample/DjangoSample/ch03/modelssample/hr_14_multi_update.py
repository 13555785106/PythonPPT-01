#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()
from ch03.modelssample.hr import *
from django.db.models import F

"""
批量更新
"""

print Emp.objects.all().update(salary=F('salary') + 1000)
