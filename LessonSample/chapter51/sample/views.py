# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from datetime import date
import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from sample.forms import *


def helloworld01(request):
    print request.build_absolute_uri('/ggg/ggg')
    for v in request.__iter__():
        print v
    return HttpResponse("Django,hello world ! in sample")


def helloworld02(request):
    print request.resolver_match.namespace
    return render(request,
                  'sample/helloworld02.html',
                  {'title': 'Hello world!', 'message': '你好世界！'})


def template_test(request):
    print request.resolver_match.namespace
    return render(request,
                  'sample/template_test.html',
                  {'fruits': ['Apple', 'Banana', 'Orange'], 'money': u'918297398.12983',
                   'days': [date(2018, 1, 1), date(2018, 1, 2), date(2018, 1, 3), date(2018, 2, 1), date(2018, 2, 2),
                            date(2018, 3, 1), date(2018, 4, 1)],
                   'books': [
                       {'title': '1984', 'author': {'name': 'George', 'age': 45}},
                       {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
                       {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
                   ],
                   'cur_now': datetime.datetime.now().date()})


def reqattrs(request):
    return render(request,
                  'sample/reqattrs.html',
                  {'request': request})


def mylogin(request):
    print request.user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'sample/login.html')


def upload(request):
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            user = request.POST.get('user')
            img = request.FILES.get('img')
            f = open(os.path.join('media', img.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            ret['status'] = True
            ret['data'] = os.path.join('media', img.name)
        except Exception as e:
            ret['error'] = e
        finally:
            f.close()
            return HttpResponse(json.dumps(ret))
    return render(request, 'sample/upload.html')


def formtest(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print form['name'].value()
            form.save()
        else:
            print form.errors.as_json()

    return render(request, 'sample/formtest.html', {'form': form})


def test_tag(request, year, month):
    cities = [
        {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
        {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
        {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
        {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
        {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]
    m = ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]
    return render(request,
                  'sample/test_tag.html',
                  {'cities': cities, "m": m})


def tag_autoescape(request):
    return render(request,
                  'sample/tag_autoescape.html',
                  {'message': """<a href="http://www.163.com">网易</a>"""})


def tag_comment(request):
    return render(request,
                  'sample/tag_comment.html',
                  {'pub_date': datetime.now()})


def tag_circle(request):
    return render(request,
                  'sample/tag_circle.html',
                  {'fruits': ['苹果', '香蕉', '桃子', '草莓', '西瓜', '芒果', '鸭梨', '葡萄'], 's1': 'I', 's2': 'II'})


def tag_filter(request):
    return render(request,
                  'sample/tag_filter.html',
                  {})


def tag_firstof(request):
    return render(request,
                  'sample/tag_firstof.html',
                  {'var1': 1, 'var2': 'Hello'})


def tag_for(request):
    return render(request,
                  'sample/tag_for.html',
                  {'fruits': ['苹果', '香蕉', '桃子', '草莓', '西瓜', '芒果', '鸭梨', '葡萄']})


def tag_if(request):
    return render(request,
                  'sample/tag_if.html',
                  {'score': 78, 'password': '1234567890', 'fruits': ['苹果', '香蕉', '桃子', '桃子', '桃子', '芒果', '芒果', '芒果']})


def tag_now(request):
    return render(request,
                  'sample/tag_now.html',
                  {})


class AuthorList(ListView):
    model = Author

    def get_context_data(self, **kwargs):
        print self.args
        # Call the base implementation first to get a context
        context = super(AuthorList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['name'] = 'xiaojf'
        return context
