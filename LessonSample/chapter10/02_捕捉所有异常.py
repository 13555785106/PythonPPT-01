#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    num = 100 / 0
    fh = open("testfile", "r")
    print fh.readline()
except:  # 捕捉所有类型的异常
    print "运行失败了!"
else:
    print "读文件成功!"
    fh.close()
