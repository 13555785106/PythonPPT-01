# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-07 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch05', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hobbies',
            field=models.ManyToManyField(to='ch05.Hobby'),
        ),
    ]
