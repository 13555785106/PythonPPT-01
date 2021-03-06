# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-09 11:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ch06', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userextra',
            options={'verbose_name': '\u7528\u6237\u9644\u52a0\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u9644\u52a0\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='userextra',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='userextra',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u90ae\u4ef6'),
        ),
        migrations.AlterField(
            model_name='userextra',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='userextra',
            name='sex',
            field=models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], default='\u7537', max_length=8, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='userextra',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
    ]
