#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^helloworld01/', views.helloworld01, name="helloworld01"),
    url(r'^helloworld02/', views.helloworld02),
    url(r'^template_test/', views.template_test),
    url(r'^reqattrs/', views.reqattrs),
    url(r'^test_tag/(?P<year>\d{4})/(?P<month>\d{1,2})$', views.test_tag, name='test_tag'),
    url(r'^tag_autoescape', views.tag_autoescape),
    url(r'^tag_comment', views.tag_comment),
    url(r'^tag_circle', views.tag_circle),
    url(r'^tag_filter', views.tag_filter),
    url(r'^tag_fisrtof', views.tag_firstof),
    url(r'^tag_for', views.tag_for),
    url(r'^tag_if', views.tag_if),
    url(r'^tag_now', views.tag_now),
    url(r'^formtest', views.formtest),
    url(r'^upload', views.upload),
    url(r'^login', views.mylogin),
    url(r'^authors/([\w-]+)/([\w-]+)/$', views.AuthorList.as_view()),
]
