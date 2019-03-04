#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from ch01 import views

"""
url调度配置文件
"""
app_name = 'ch01'
urlpatterns = [
    url(r'^index/', views.index, name="index"),
    # ex: /ch01/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /ch01/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /ch01/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
