#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "r")
    print fh.readline()
    num = 100 / 0
except (IOError, ZeroDivisionError), e:  # 捕捉多种类型的异常
    if isinstance(e, ZeroDivisionError):
        print "除数不能为0!"
    elif isinstance(e, IOError):
        print "读文件失败!"

else:
    print "读文件成功!"
    fh.close()
