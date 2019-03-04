# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-11 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ch03', '0013_auto_20190111_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(related_name='entries', to='ch03.Author'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='ch03.Blog'),
        ),
    ]
