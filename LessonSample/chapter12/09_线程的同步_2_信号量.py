#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time


# 为线程定义一个函数
def worker(s):
    s.acquire()
    print threading.current_thread().name + ' 进入'
    time.sleep(5)
    print threading.current_thread().name + ' 离开'
    s.release()


semaphore = threading.Semaphore(2)
for i in xrange(10):
    t = threading.Thread(target=worker, args=(semaphore,))
    t.setName('线程 ' + str(i))
    t.start()
