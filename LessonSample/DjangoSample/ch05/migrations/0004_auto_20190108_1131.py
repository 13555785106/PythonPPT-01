# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-08 11:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch05', '0003_auto_20190108_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(2019, 1, 8), null=True),
        ),
    ]
