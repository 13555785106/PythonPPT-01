#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from ch06 import views

app_name = 'ch06'
urlpatterns = [
    url(r'^user_extra_detail/(?P<id>\d+)$', views.user_extra_detail, name="user_extra_detail"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
]
