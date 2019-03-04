#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from ch03 import views

app_name = 'ch03'
urlpatterns = [
    url(r'^index/', views.index, name="index"),
]
