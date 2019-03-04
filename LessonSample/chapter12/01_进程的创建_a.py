#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import multiprocessing
import os
import time

'''
multiprocessing 库
跨平台版本的多进程模块,提供了一个Process类来代表一个进程对象
'''


def run():
    for i in xrange(10):
        print '子进程 pid=%-8s %s' % (os.getpid(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        time.sleep(5)


p = multiprocessing.Process(target=run)  # 创建子进程

p.start()  # 启动进程
for i in xrange(10):
    print '主进程 pid=%-8s %s' % (os.getpid(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(5)
