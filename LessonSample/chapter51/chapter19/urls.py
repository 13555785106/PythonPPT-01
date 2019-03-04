#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""chapter19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from chapter19 import settings
# 只有在非调试状态下起作用，想测试效果请使用uWSGI运行
handler404 = 'chapter19.views.my404'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sample/', include('sample.urls', 'n01')),
    url(r'^sample01/', include('sample01.urls', 'n02')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
