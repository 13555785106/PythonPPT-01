# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Dep(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return 'id=%s,name=%s' % (self.id, self.name)


@python_2_unicode_compatible
class Job(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128)
    min_salary = models.DecimalField(max_digits=9, decimal_places=2)
    max_salary = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.id


@python_2_unicode_compatible
class Emp(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=128)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    commission_pct = models.FloatField(null=True)
    manager_id = models.IntegerField(default=-1)
    dep = models.ForeignKey(Dep, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'id=%s,name=%s' % (self.id, (self.first_name + ' ' + self.last_name))


@python_2_unicode_compatible
class SalGrade(models.Model):
    level = models.CharField(primary_key=True, max_length=32)
    min_salary = models.DecimalField(max_digits=9, decimal_places=2)
    max_salary = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.level
