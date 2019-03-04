# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import uuid

from django.contrib.auth.models import User
from django.core.validators import *
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

SEXES = (('男', '男'), ('女', '女'))


def validate_mobile(value):
    if not re.match(r'\d+', value):
        raise ValidationError(
            '%(value)s 不是有效手机号码',
            params={'value': value}, code='invalid'
        )


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)


@python_2_unicode_compatible
class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def get_file_path(model, filename):
    dir = "%Y/%m/%d"
    dir = datetime.datetime.now().strftime(dir)

    return 'upload/' + dir + '/%s' % (filename + '.' + uuid.uuid1().hex)


@python_2_unicode_compatible
class Author(models.Model):
    class Meta:
        ordering = ["account"]
        permissions = (
            ("hit1", "Can see available tasks"),
            ("hit2", "Can change the status of tasks"),
            ("hit3", "Can remove a task by setting its status as closed"),
        )

    account = models.CharField(max_length=12, unique=True, null=False,
                               validators=[RegexValidator(r'^\w+$', '请输入字母、数字或下划线')])
    passwd = models.CharField(max_length=12, default='123', validators=[RegexValidator(r'^[0-9]+$', '请输入数字')])
    name = models.CharField(max_length=12, validators=[RegexValidator(r'^[0-9]+$', '请输入数字')])
    sex = models.CharField(max_length=8, choices=SEXES, default='男', null=False, blank=False)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=20, null=True, validators=[validate_mobile])
    annual_income = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                        validators=[MinValueValidator(0, '不能小于 %(limit_value)s')])
    hobbies = models.ManyToManyField(Hobby)
    thumbnail = models.ImageField(upload_to=get_file_path, null=True)

    def __str__(self):
        fmt = "Author(account={0},name={1},sex={2},birthday={3},email={4},mobile={5},thumbnail={6})"
        return fmt.format(self.account, self.name, self.sex, self.birthday.strftime("%Y年%m月%d日".encode('UTF-8')).decode(
            'UTF-8'), self.email, self.mobile, self.thumbnail)


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Tag(name=%s)" % (self.name)


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    release_time = models.DateTimeField()
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "Article(title={0},content={1},score={2},release_time={3},author={4},tags={5})".format(
            self.title,
            self.content,
            self.score,
            self.release_time.strftime("%Y-%m-%d %H:%M:%S"),
            self.author.name,
            ",".join([t.name for t in self.tags.all()])
        )
