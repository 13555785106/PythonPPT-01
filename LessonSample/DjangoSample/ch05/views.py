# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from django import forms
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.forms.fields import *
from django.forms.widgets import *
from django.shortcuts import redirect
from django.shortcuts import render

import DjangoSample.settings
from ch05.models import *

def index(request):
    return render(request,
                  'ch05/index.html',
                  {})


PROVINCES = (('辽', '辽宁省'), ('鲁', '山东省'), ('湘', '湖南省'))


class ContactForm(forms.Form):
    name = forms.CharField(label='姓名',max_length=5)
    province = forms.ChoiceField(label='省份',choices=PROVINCES)
    email = forms.EmailField(label='邮件')
    age = forms.IntegerField(label='年龄',min_value=1, max_value=150)


def contact(request):
    context = {}
    if request.method == 'GET':
        context['form'] = ContactForm()
    if request.method == 'POST':
        context['form'] = ContactForm(data=request.POST)
        if context['form'].is_valid():
            context['data'] = context['form'].cleaned_data
    return render(request,
                  'ch05/contact.html', context)


def list_user(request):
    users = User.objects.all().order_by('account')
    paginator = Paginator(users, 2)
    number = 0
    page = None
    if request.POST:
        if 'number' in request.POST:
            number = int(request.POST['number'])

        if 'first_page' in request.POST:
            number = 0
        elif 'last_page' in request.POST:
            number = sys.maxint
        elif 'previous_page' in request.POST:
            number -= 1
        elif 'next_page' in request.POST:
            number += 1

    if paginator.num_pages > 0:
        if number < 1:
            number = 1
        elif number > paginator.num_pages:
            number = paginator.num_pages
        page = paginator.page(number)

    return render(request,
                  'ch05/list_user.html', {'page': page})


class UserForm(ModelForm):
    confirmPasswd = CharField(max_length=512, label='确认密码', widget=PasswordInput)

    class Meta:
        model = User
        fields = ['id', 'account', 'passwd', 'confirmPasswd', 'name', 'sex', 'birthday', 'email', 'mobile',
                  'annual_income', 'hobbies', 'thumbnail']
        labels = {'id': '主键', 'account': '账号', 'passwd': '密码', 'name': '姓名', 'sex': '性别', 'birthday': '生日',
                  'email': '邮件', 'mobile': '电话', 'annual_income': '年收入',
                  'hobbies': '爱好', 'thumbnail': '头像'}
        widgets = {'id': HiddenInput(), 'passwd': PasswordInput(), 'sex': RadioSelect(),
                   'hobbies': CheckboxSelectMultiple()}

        error_messages = {
            'account': {
                'unique': '当前账号已经存在',
            },
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        print User.objects.filter(account=cleaned_data['account']).count()
        count = 0
        if self.instance.id:
            count = User.objects.filter(account=cleaned_data['account']).exclude(id=self.instance.id).count()
        else:
            count = User.objects.filter(account=cleaned_data['account']).count()

        if count > 0:
            self.add_error('account', '账号 %s 已经存在' % cleaned_data['account'])

        if cleaned_data['passwd'] != cleaned_data['confirmPasswd']:
            self.add_error('confirmPasswd', '确认密码与密码不同')


def add_user(request):
    form = UserForm(label_suffix=" : ")
    if request.POST:
        form = UserForm(data=request.POST, files=request.FILES, label_suffix=" : ")
        if form.is_valid():
            form.save()
            return redirect(reverse('ch05:list_user', args=[]))

    return render(request,
                  'ch05/add_user.html', {'form': form})


def chg_user(request, id):
    form = None
    user = User.objects.get(pk=id)
    old_url = user.thumbnail.url
    if request.method == 'GET':
        form = UserForm(instance=user, label_suffix=" : ")
    elif request.method == 'POST':
        form = UserForm(data=request.POST, files=request.FILES, instance=user, label_suffix=" : ")
        if form.is_valid():
            form.save()
            os.remove(DjangoSample.settings.BASE_DIR + old_url)
            return redirect(reverse('ch05:list_user', args=[]))
    return render(request,
                  'ch05/chg_user.html', {'form': form})


def del_user(request, id):
    user = User.objects.get(pk=id)

    user.delete()
    os.remove(DjangoSample.settings.BASE_DIR + user.thumbnail.url)
    return redirect(reverse('ch05:list_user', args=[]))
