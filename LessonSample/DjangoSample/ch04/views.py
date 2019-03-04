# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from ch03.models import *


def index(request):
    return render(request,
                  'ch04/index.html',
                  {})


def autoescape_tag(request):
    return render(request,
                  'ch04/autoescape_tag.html',
                  {'msg': """<span style="color:red">文本信息</span>"""})


def comment_tag(request):
    return render(request,
                  'ch04/comment_tag.html',
                  {'msg': """<span style="color:red">文本信息</span>"""})


def template(request):
    return render(request,
                  'ch04/template.html',
                  {'nums': [1, 2, 3, 4, 5]})


def filter_tag(request):
    return render(request,
                  'ch04/filter_tag.html',
                  {
                      'msg': """<span style="color:red"> Apple Banana</span>"""
                  })


def for_tag(request):
    return render(request,
                  'ch04/for_tag.html',
                  {
                      'authors': Author.objects.order_by('name'),
                      'dict': {'apple': '苹果', 'banane': '香蕉', 'peach': '桃子'}
                  })


def for_empty_tag(request):
    return render(request,
                  'ch04/for_empty_tag.html',
                  {'authors': Author.objects.filter(email__endswith='163.comt').order_by('name')})


def firstof_tag(request):
    return render(request,
                  'ch04/firstof_tag.html',
                  {'var2': 2, 'var3': 3, 'var5': 5, })


def if_tag(request):
    return render(request,
                  'ch04/if_tag.html',
                  {'score': 76})


def ifchanged_tag(request):
    return render(request,
                  'ch04/ifchanged_tag.html',
                  {'nums': (0, 0, 1, 1, 1, 2, 2)})


def now_tag(request):
    return render(request,
                  'ch04/now_tag.html',
                  {})


def lorem_tag(request):
    return render(request,
                  'ch04/lorem_tag.html',
                  {})


def regroup_tag(request):
    return render(request,
                  'ch04/regroup_tag.html',
                  {'cities': [
                      {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
                      {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
                      {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
                      {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
                      {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
                  ]})


def spaceless_tag(request):
    return render(request,
                  'ch04/spaceless_tag.html',
                  {})


def with_tag(request):
    return render(request,
                  'ch04/with_tag.html',
                  {})


def withratio_tag(request):
    return render(request,
                  'ch04/withratio_tag.html',
                  {'this_value': 100, 'max_value': 200, 'max_width': 512})


def verbatim_tag(request):
    return render(request,
                  'ch04/verbatim_tag.html',
                  {})


def url_tag(request):
    return render(request,
                  'ch04/url_tag.html',
                  {})


def url_tag_test(request, a, b):
    return HttpResponse('a=' + a + ',b=' + b)


def circle_tag(request):
    return render(request,
                  'ch04/circle_tag.html',
                  {'nums': [x + 1 for x in xrange(10)]})


def custom_tag(request):
    return render(request,
                  'ch04/custom_tag.html',
                  {'line': 'Removes all values of arg from the given string',
                   'fruits': ['apple', 'banana', 'peach']})


def filters(request):
    return render(request,
                  'ch04/filters.html',
                  {
                      'value': 100,
                      'digits': '0123456789',
                      'msg01': "I'm using Django",
                      'msg02': "a apple banana peach",
                      'novalue': None,
                      'now': datetime.now(),
                      'dt01': datetime.strptime('2018-1-1 12:12:12', "%Y-%m-%d %H:%M:%S"),
                      'dt02': datetime.strptime('2018-1-3 13:34:45', "%Y-%m-%d %H:%M:%S"),
                      'dt03': datetime.strptime('2019-8-3 13:34:45', "%Y-%m-%d %H:%M:%S"),
                      'students': [
                          {'name': 'zed', 'age': 19},
                          {'name': 'amy', 'age': 22},
                          {'name': 'joe', 'age': 31},
                      ],
                      'paragraph': 'Python\n是有趣强大的<b>语言</b>\nJava\n也是有趣强大的<b>语言</b>',
                      'javascript': """function disp_prompt()
  {
  var name=prompt("请输入您的名字","Bill Gates")
  if (name!=null && name!="")
    {
    document.write("你好！" + name + " 今天过得怎么样？")
    }
  }""",
                      'uri': 'https://www.example.org/foo?a=b&c=d&name=大家拿',
                      'words': ['apple', 'banana', 'peach'],
                      'provinces':['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
                  })
