#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

from ch04 import views

app_name = 'ch04'
urlpatterns = [
    url(r'^index/', views.index, name="index"),
    url(r'^template/', views.template, name="template"),
    url(r'^autoescape_tag/', views.autoescape_tag, name="autoescape_tag"),
    url(r'^comment_tag/', views.comment_tag, name="comment_tag"),
    url(r'^for_tag/', views.for_tag, name="for_tag"),
    url(r'^for_empty_tag/', views.for_empty_tag, name="for_empty_tag"),
    url(r'^filter_tag/', views.filter_tag, name="filter_tag"),
    url(r'^firstof_tag/', views.firstof_tag, name="firstof_tag"),
    url(r'^if_tag/', views.if_tag, name="if_tag"),
    url(r'^ifchanged_tag/', views.ifchanged_tag, name="ifchanged_tag"),
    url(r'^now_tag/', views.now_tag, name="now_tag"),
    url(r'^lorem_tag/', views.lorem_tag, name="lorem_tag"),
    url(r'^regroup_tag/', views.regroup_tag, name="regroup_tag"),
    url(r'^spaceless_tag/', views.spaceless_tag, name="spaceless_tag"),
    url(r'^with_tag/', views.with_tag, name="with_tag"),
    url(r'^withratio_tag/', views.withratio_tag, name="withratio_tag"),
    url(r'^verbatim_tag/', views.verbatim_tag, name="verbatim_tag"),
    url(r'^url_tag/', views.url_tag, name="url_tag"),
    url(r'^url_tag_test/(?P<a>[0-9]+)/(?P<b>[0-9]+)/$', views.url_tag_test, name="url_tag_test"),
    url(r'^circle_tag/', views.circle_tag, name="circle_tag"),
    url(r'^custom_tag/', views.custom_tag, name="custom_tag"),
    url(r'^filters/', views.filters, name="filters"),
]
