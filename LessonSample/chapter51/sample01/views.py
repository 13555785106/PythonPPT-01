# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

def helloworld01(request):
    return HttpResponse("Django,hello world ! in sample01")


def helloworld02(request):
    print request.resolver_match.namespace
    return render(request,
                  'sample/helloworld02.html',
                  {'title': 'Hello world!', 'message': '你好世界！'})
