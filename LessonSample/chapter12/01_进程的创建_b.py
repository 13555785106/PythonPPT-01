#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

print '***************************'
ret = os.fork()  # 返回值等于0时，子进程
print '###########################'
if ret > 0:
    print("%d---主进程---%d---%d---" % (ret,os.getpid(), os.getppid()))
else:
    print("%d---子进程---%d---%d---" % (ret,os.getpid(), os.getppid()))
print '^^^^^^^^^^^^^^^^^^^^^^^^^^^'
