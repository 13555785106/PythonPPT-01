# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-17 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ch01', '0002_auto_20190109_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=128)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('commission_pct', models.FloatField(null=True)),
                ('manager_id', models.IntegerField(default=-1)),
                ('dep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ch01.Dep')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='SalGrade',
            fields=[
                ('level', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.AddField(
            model_name='emp',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ch01.Job'),
        ),
    ]
