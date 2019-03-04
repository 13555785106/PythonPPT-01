#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time


# 为线程定义一个函数
def worker(lock):
    for i in xrange(10):
        time.sleep(1)
        lock.acquire()
        print threading.current_thread().name
        lock.release()


lock = threading.Lock()
for i in xrange(5):
    t = threading.Thread(target=worker, args=(lock,))
    t.setName('线程 ' + str(i))
    t.start()
