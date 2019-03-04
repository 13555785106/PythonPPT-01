# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import django
from django import forms

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSample.settings")
django.setup()

PROVINCES = (('辽', '辽宁省'), ('鲁', '山东省'), ('湘', '湖南省'))


class ContactForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=5)
    province = forms.ChoiceField(label='省份', choices=PROVINCES)
    email = forms.EmailField(label='邮件')
    age = forms.IntegerField(label='年龄', min_value=1, max_value=150)


data = {
    'name': '肖俊峰rrrr',
    'province': '辽',
    'email': 'w@w',
    'age': 909
}

f = ContactForm(initial={'name': '肖俊峰', 'province': '辽1', 'email': 'w@w', 'age': 900}, data=data)
# print dir(f)
# 判断表单数据是否有效
print f.is_valid()
# 判断表单数据对于初始数据是否发生变化
print f.has_changed()

# 打印字段错误信息
for k, v in f.errors.items():
    print k, v, type(v)
# 打印非字段错误信息
for v in f.non_field_errors():
    print v, type(v)
