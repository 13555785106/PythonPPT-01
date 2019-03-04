#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urlparse

url = 'http://user:passwd@www.163.com:80/path01/path02;param01=01;param02=02?arg1=01&arg2=02#fragment'

pr = urlparse.urlparse(url)
print pr
print urlparse.urlunparse(pr)

sr = urlparse.urlsplit(url)
print sr
print urlparse.urlunsplit(sr)

print urlparse.urljoin('https://baidu.com/vote/', '9999')

print urlparse.parse_qs('name=xiaojf&age=45')
print urlparse.parse_qsl('name=xiaojf&age=45')

print urlparse.urldefrag(url)
# /不转，空格转成%20，适合POST方式
s1 = urllib.quote("/中国abc / 辽宁def")
print s1
print urllib.unquote(s1)
# /转%2F，空格转成+号，适合GET方式
s2 = urllib.quote_plus("/中国abc / 辽宁def")
print s2
print urllib.unquote_plus(s2)

params = urllib.urlencode({'name': '俊峰 肖', 'age': 45, 'sex': '男'})
print params


print urlparse.urljoin('https://baidu.com/vote/', '#9999')