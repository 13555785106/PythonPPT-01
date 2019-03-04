# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-07 20:43
from __future__ import unicode_literals

import ch05.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=64, unique=True)),
                ('passwd', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=12)),
                ('sex', models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], default='\u7537', max_length=8)),
                ('birthday', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('annual_income', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('thumbnail', models.ImageField(null=True, upload_to=ch05.models.get_file_path)),
                ('hobbies', models.ManyToManyField(null=True, to='ch05.Hobby')),
            ],
        ),
    ]