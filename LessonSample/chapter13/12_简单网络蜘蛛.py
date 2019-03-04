#!/usr/bin/python
# -*- coding: UTF-8 -*-
import httplib
import urllib2

from lxml import etree

url = 'http://www.163.com'

request = urllib2.Request(url)

# urlopen函数如果传递参数，就以POST参数传递
response = urllib2.urlopen(request)
if response.getcode() == httplib.OK:
    contentType = response.info()['Content-Type']
    charset = ''
    if contentType:
        pos = contentType.find('=')
        if pos != -1:
            charset = contentType[pos + 1:]
    html = response.read()
    if charset:
        html = html.decode(charset)

    for href in etree.HTML(html).xpath("//a/@href"):
        print href
