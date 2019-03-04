# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-11 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch03', '0011_auto_20190111_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(default='--', max_length=8192),
        ),
        migrations.AlterField(
            model_name='entry',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]