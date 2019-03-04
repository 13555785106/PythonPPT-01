# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def print_session_info(request):
    user = authenticate(request, username='xiaojf', password='xjfdlj2010')
    print user.username,user.backend
    # print dir(request.session)
    #print type(request.session.keys)
    print request.session.session_key

    for k, v in request.session.items():
        print k, v
    return render(request, 'print_session_info.html', {'session': request.session})
