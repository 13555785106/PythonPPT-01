#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

# 遍历当前工作目录
for root, dirs, files in os.walk('.'):
    for name in files:
        print u'文件 ' + root + os.sep + name.decode("GBK")
    for name in dirs:
        print u'目录 ' + root + os.sep + name.decode('GBK')
