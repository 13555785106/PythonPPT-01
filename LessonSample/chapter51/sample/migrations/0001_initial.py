# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-22 21:00
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sample.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('release_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^\\w+$', '\u8bf7\u8f93\u5165\u5b57\u6bcd\u3001\u6570\u5b57\u6216\u4e0b\u5212\u7ebf')])),
                ('passwd', models.CharField(default='123', max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]+$', '\u8bf7\u8f93\u5165\u6570\u5b57')])),
                ('name', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]+$', '\u8bf7\u8f93\u5165\u6570\u5b57')])),
                ('sex', models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], default='\u7537', max_length=8)),
                ('birthday', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=20, null=True, validators=[sample.models.validate_mobile])),
                ('annual_income', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0, '\u4e0d\u80fd\u5c0f\u4e8e %(limit_value)s')])),
                ('thumbnail', models.ImageField(null=True, upload_to=sample.models.get_file_path)),
            ],
            options={
                'permissions': (('hit1', 'Can see available tasks'), ('hit2', 'Can change the status of tasks'), ('hit3', 'Can remove a task by setting its status as closed')),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='hobbies',
            field=models.ManyToManyField(to='sample.Hobby'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='sample.Tag'),
        ),
    ]