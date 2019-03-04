#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib

line = 'http://www.163jsp.com?' + urllib.quote('name= Tom &age=30&sex=男')
print line
line = urllib.unquote(line)
print line

line = 'http://www.163jsp.com?' + urllib.quote_plus('name= Tom &age=30&sex=男')
print line
line = urllib.unquote_plus(line)
print line

print urllib.urlencode({'name': ' Tom ', 'sex': '男'})
