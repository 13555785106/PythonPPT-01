#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^helloworld01/', views.helloworld01, name="helloworld01"),
    url(r'^helloworld02/', views.helloworld02, name="helloworld02"),
]
