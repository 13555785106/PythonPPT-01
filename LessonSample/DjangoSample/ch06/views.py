# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render

from models import UserExtra


# Create your views here.
def user_extra_detail(request, id):
    user_extra = UserExtra.objects.get(pk=id)
    return render(request,
                  'ch06/user_extra_detail.html',
                  {'user_extra': user_extra})


class LoginForm(forms.Form):
    username = forms.CharField(label='账号', max_length=64)
    password = forms.CharField(label='密码', max_length=64)


def login(request):
    form = None
    if request.session.get('_auth_user_id', default=None):
        pass
    else:
        if request.method == 'GET':
            form = LoginForm()
        elif request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user:
                    request.session['_auth_user_id'] = user.id
                    request.session['_auth_user_hash'] = user.get_session_auth_hash()
                    request.session['_auth_user_backend'] = user.backend
                    form = None

    return render(request,
                  'ch06/login.html',
                  {'form': form})


def logout(request):
    if request.session:
        request.session.flush()
    return redirect("ch06:login")
