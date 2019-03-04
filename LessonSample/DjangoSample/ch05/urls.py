#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from ch05 import views

app_name = 'ch05'
urlpatterns = [
    url(r'^index', views.index, name="index"),
    url(r'^list_user', views.list_user, name="list_user"),
    url(r'^add_user', views.add_user, name="add_user"),
    url(r'^chg_user/(?P<id>\d+)$', views.chg_user, name="chg_user"),
    url(r'^del_user/(?P<id>\d+)$', views.del_user, name="del_user"),
    url(r'^contact', views.contact, name="contact"),
]
