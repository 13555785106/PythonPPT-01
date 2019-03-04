#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time


# 为线程定义一个函数
def worker(e):
    for x in xrange(5):
        print threading.current_thread().name + ' 进入'
        e.wait()
        print threading.current_thread().name + ' 离开'


event = threading.Event()
for i in xrange(5):
    t = threading.Thread(target=worker, args=(event,))
    t.setName('线程 ' + str(i))
    t.start()
for v in xrange(5):
    time.sleep(5)
    event.set()
    event.clear()
