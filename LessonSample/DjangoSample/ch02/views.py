# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'ch02/index.html', {})


def hello_world_01(request):
    return HttpResponse("Hello world !<a href='../index'>返回</a>")


def hello_world_02(request):
    return render(request,
                  'ch02/hello_world_02.html',
                  {'title': 'Hello world!', 'message': 'Hello world!'})


def req_attrs(request):
    return render(request,
                  'ch02/req_attrs.html',
                  {})


@csrf_exempt
def req_parameters(request):
    name, age = '', ''
    if request.GET:
        name = request.GET['name']
        age = request.GET['age']
    if request.POST:
        name = request.POST['name']
        age = request.POST['age']

    resp = {'name': name, 'age': age}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def upload(request):
    context = {}
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            img = request.FILES.get('img')
            f = open(os.path.join('media', img.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            f.close()
            context = {'name': name, 'img': img.name}
        except IOError:
            print "Error: 没有找到文件或读取文件失败"
    return HttpResponse(json.dumps(context), content_type="application/json")


def req_parameters_01(request):
    name, age = '', ''
    if request.GET:
        name = request.GET['name']
        age = request.GET['age']
    if request.POST:
        name = request.POST['name']
        age = request.POST['age']

    return render(request,
                  'ch02/req_parameters_01.html', {'name': name, 'age': age})


def req_parameters_02(request, name, age):
    return render(request,
                  'ch02/req_parameters_02.html', {'name': name, 'age': age})


def simple_resp(request):
    response = HttpResponse()
    response.status_code = 200
    response['Content-Type'] = 'text/html; charset=utf-8'
    response['User-Defined-Header'] = '这是我自定义的头'
    name = urlquote('肖俊峰')
    response.set_cookie('name', name)
    response.content = loader.render_to_string('ch02/simple_resp.html', {'message': '我们只有自己拯救自己！'}, request)
    return response


def resp_404(request):
    raise Http404('非常抱歉，你请求的页面找不到。')
    # return HttpResponseNotFound()


def resp_redirect(request):
    return HttpResponseRedirect("http://www.163.com")


def read_big_file(fn, buf_size=8192):
    try:
        f = open(fn, "rb")
        while True:
            buf = f.read(buf_size)
            if buf:
                yield buf
            else:
                break
        f.close()
    except IOError:
        print "Error: 没有找到文件或读取文件失败"


def resp_download(request):
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'score.xls')
    response = HttpResponse()
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment; filename="score.xls"'
    response['Content-Length'] = os.path.getsize(filename)
    response.content = read_big_file(filename)
    return response


def file_upload(request):
    context = {}
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            img = request.FILES.get('img')
            f = open(os.path.join('media', img.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            f.close()
            context = {'name': name, 'img': img.name}
        except IOError:
            print "Error: 没有找到文件或读取文件失败"
    return render(request, 'ch02/for_tag.html', context)
