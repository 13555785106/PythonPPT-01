# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-11 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch03', '0012_auto_20190111_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=8192),
        ),
    ]
