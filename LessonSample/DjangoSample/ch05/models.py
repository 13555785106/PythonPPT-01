# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import os.path
import uuid

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

SEXES = (('男', '男'), ('女', '女'))


def get_file_path(model, filename):
    return 'upload/' + datetime.datetime.now().strftime("%Y/%m/%d") + '/%s' % (
            uuid.uuid1().hex + os.path.splitext(filename)[1])


@python_2_unicode_compatible
class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=64, unique=True)
    passwd = models.CharField(max_length=512)
    name = models.CharField(max_length=12)
    sex = models.CharField(max_length=8, choices=SEXES, default='男', null=False, blank=False)
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hobbies = models.ManyToManyField(to=Hobby, blank=True)
    thumbnail = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'id=%s' % (self.id,)
