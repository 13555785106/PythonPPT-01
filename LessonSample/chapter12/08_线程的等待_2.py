#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

"""将主线程设置为子线程的守护线程"""
print '主线程开始'


# 为线程定义一个函数
def print_info(seconds):
    for i in xrange(seconds):
        time.sleep(1)
        print threading.current_thread().name


for i in xrange(5):
    t = threading.Thread(target=print_info, args=(5,))
    t.setDaemon(True)
    t.setName('线程 ' + str(i))
    t.start()

print '主线程结束'
