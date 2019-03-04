# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def helloworld01(request):
    return HttpResponse("Django,hello world ! ")


def helloworld02(request):
    return render(request,
                  'sample/helloworld02.html',
                  {'title': 'Hello world!', 'message': '你好世界！'})


def reqattrs(request):

    return render(request,
                  'sample/reqattrs.html',
                  {'request': request})
