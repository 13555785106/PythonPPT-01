# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-08 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch05', '0012_auto_20190108_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
