#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from ch02 import views

app_name = 'ch02'
urlpatterns = [
    url(r'^index/', views.index, name="index"),
    url(r'^hello_world_01/', views.hello_world_01, name="hello_world_01"),
    url(r'^hello_world_02/', views.hello_world_02, name="hello_world_02"),
    url(r'^req_attrs/', views.req_attrs, name="req_attrs"),
    url(r'^upload', views.upload, name="upload"),
    url(r'^req_parameters', views.req_parameters, name="req_parameters"),
    url(r'^req_parameters_01', views.req_parameters_01, name="req_parameters_01"),
    url(r'^req_parameters_02/(?P<name>.+)/(?P<age>\d+)$', views.req_parameters_02, name="req_parameters_02"),
    url(r'^simple_resp', views.simple_resp, name="simple_resp"),
    url(r'^resp_404', views.resp_404, name="resp_404"),
    url(r'^resp_redirect', views.resp_redirect, name="resp_redirect"),
    url(r'^resp_download', views.resp_download, name="resp_download"),
    url(r'^file_upload', views.file_upload, name="file_upload"),
]
