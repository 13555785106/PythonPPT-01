# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

"""
模型定义文件
"""


# python manage.py makemigrations ch01
# python manage.py sqlmigrate ch01 0001
# python manage.py migrate
# python manage.py shell
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('发布日期')

    def was_published_recently(self):
        now = datetime.now()
        past = now - timedelta(hours=72)
        return past <= self.pub_date <= now

    was_published_recently.short_description = '最新发布?'
    was_published_recently.boolean = True

    def pub_date_str(self):
        return self.pub_date.strftime("%Y-%m-%d %H:%M:%S")

    pub_date_str.short_description = '发布日期'
    pub_date_str.admin_order_field = 'pub_date'

    class Meta:
        verbose_name = "问题表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question_text


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项', max_length=200)
    votes = models.IntegerField('票数', default=0)

    def __str__(self):
        return self.choice_text


