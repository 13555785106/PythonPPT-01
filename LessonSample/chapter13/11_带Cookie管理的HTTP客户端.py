#!/usr/bin/python
# -*- coding: UTF-8 -*-
import httplib, urllib, urllib2, cookielib

cookie = cookielib.CookieJar()
# 加入urllib2处理cookie的能力
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
parameters = urllib.urlencode({'name': '肖俊峰', 'age': 45})
url = 'http://192.168.3.9:9090/12306/Test'

request = urllib2.Request(url, parameters)

# 第一次请求存在设置cookie的头信息，以后的请求则不存在
for i in xrange(5):
    response = urllib2.urlopen(request)
    if response.getcode() == httplib.OK:
        for k, v in response.info().items():
            print "[%s],[%s]" % (k, v)
        html = response.read()
        print html
        print dir(cookie)

# 对于上传文件可自己尝试编写，前提是你对HTTP协议有关上传文件的内容要清楚。
# request.add_header('cookie', 'JSESSIONID=43A00F1D3FE84F956377A4EBC646AFD5')
