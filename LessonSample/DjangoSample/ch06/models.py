# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import *
from django.core.urlresolvers import reverse

SEXES = (('男', '男'), ('女', '女'))


class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    sex = models.CharField(max_length=8, choices=SEXES, default='男', null=False, blank=False, verbose_name='性别')
    birthday = models.DateField(blank=True, null=True, verbose_name='生日')
    email = models.EmailField(blank=True, null=True, verbose_name='邮件')
    mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name='电话')

    class Meta:
        verbose_name = "用户附加信息"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('ch06:user_extra_detail', args=[self.pk])

    def __str__(self):
        return self.user.username
