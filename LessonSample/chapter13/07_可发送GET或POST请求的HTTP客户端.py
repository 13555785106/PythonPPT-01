#!/usr/bin/python
# -*- coding: UTF-8 -*-
import httplib, urllib, urllib2

parameters = urllib.urlencode({'name': '肖俊峰', 'age': 45})
url = 'http://192.168.3.9:9090/12306/Test'

request = urllib2.Request(url, parameters)

# urlopen函数如果传递参数，就以POST参数传递
response = urllib2.urlopen(request)
if response.getcode() == httplib.OK:
    for k, v in response.info().items():
        print "[%s],[%s]" % (k, v)
    html = response.read()
    print html

# 对于上传文件可自己尝试编写，前提是你对HTTP协议有关上传文件的内容要清楚。
