# -*- coding: utf-8 -*-
from django.utils.encoding import *
from django.utils.http import *

print type(smart_text('大中国abc123'))
print type(force_text('大中国abc123'))
print smart_bytes('大中国abc123')
print smart_bytes(u'大中国abc123')
print uri_to_iri('http://中国.com?name=肖俊峰++--')
print iri_to_uri(u'/favorites/François/%s' % urlquote('Paris & Orléans'))
print urlquote(' http://中国.com?name=肖 俊 峰++--')
print urlquote_plus(' http://中国.com?name=肖 俊 峰++--')

import os

for root, dirs, files in os.walk('.'):
    for name in files:
        print '文件 ', root, name
    for name in dirs:
        print '目录 ', root, name

fo = open('python.txt')
print fo.readline(),
print fo.readline(),
print fo.readline(),
print fo.readline(),
print fo.readline(),
print fo.readline(),
print fo.readline(),
print fo.readline(),
print fo.readline(),
fo.close()


