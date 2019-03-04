#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "r")
    print fh.readline()
except IOError, e:  # 出现异常进入此代码块
    print type(e), e
    print '读文件失败了!'
else:  # 进入try块没有发生异常进入此代码块
    print "读文件成功!"
    fh.close()
finally:
    print '读文件完毕！'
