# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField('名', max_length=30)
    last_name = models.CharField('姓', max_length=30)
    shirt_size = models.CharField('衣服型号', max_length=1, choices=SHIRT_SIZES)
    birthday = models.DateField('生日')
    salary = models.DecimalField('工资', max_digits=9, decimal_places=2, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


@python_2_unicode_compatible
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return 'pid=%s,gid=%s' % (self.person, self.group)
