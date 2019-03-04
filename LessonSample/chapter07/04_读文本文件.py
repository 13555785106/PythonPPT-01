#!/usr/bin/python
# -*- coding: UTF-8 -*-

fo = None
try:
    fo = open("foo.txt", "r")
    print fo.read()
except:
    print '读取文件发生错误！'
finally:
    if fo:
        print dir(fo)
        fo.close()
