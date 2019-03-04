#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm
from django.forms import widgets

from models import *


@python_2_unicode_compatible
class AuthorForm(ModelForm):
    confirm_passwd = forms.CharField(label='确认密码:', max_length=12, widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ['account', 'passwd', 'confirm_passwd', 'name', 'sex', 'birthday', 'email', 'mobile', 'annual_income',
                  'hobbies', 'thumbnail']
        labels = {
            'account': '账号',
            'name': '姓名',
            'passwd': '密码',
            'sex': '性别',
            'birthday': '生日',
            'email': '邮件',
            'mobile': '手机',
            'annual_income': '年收入',
            'hobbies': '爱好',
        }
        help_texts = {
            'name': '此处输入作者的姓名',
        }
        error_messages = {
            'account': {
                'unique': "当前账号已存在。",
            },
            'name': {
                'max_length': "名字太长了.",
            },
            'birthday': {
                'invalid': "日期格式错误.",
            },
        }

        widgets = {
            'sex': widgets.RadioSelect(),
            'hobbies': widgets.CheckboxSelectMultiple(),
            'thumbnail': widgets.ClearableFileInput(attrs={'multiple': True}),
        }

    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)

    #
    def clean_annual_income(self):
        val = self.cleaned_data['annual_income']
        print val
        # 此处必须抛出单个异常
        if val > 100:
            raise ValidationError(
                '年收入不能大于100',
                params={'val': val},
                code='invalid'
            )

        return val

    def clean(self):
        cleaned_data = ModelForm.clean(self)

        print dir(self.fields['confirm_passwd'])
        print str(self.fields['confirm_passwd'])
        print self.data
        passwd = cleaned_data.get("passwd")
        confirm_passwd = cleaned_data.get("confirm_passwd")
        if passwd != confirm_passwd:
            # self.add_error('confirm_passwd', "Password does not match")
            raise ValidationError({'confirm_passwd': ValidationError(
                '确认密码 %(confirm_passwd)s 与密码 %(passwd)s 不等',
                params={'passwd': passwd, 'confirm_passwd': confirm_passwd},
                code='invalid'
            )})
            '''raise ValidationError({
                'confirm_passwd': ValidationError('确认密码错误.', code='invalid'),
            })'''

    def __str__(self):
        return "AuthorForm"
