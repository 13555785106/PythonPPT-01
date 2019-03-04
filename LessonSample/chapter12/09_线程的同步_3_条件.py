#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time


# 为线程定义一个函数
def worker(c):
    c.acquire()
    print threading.current_thread().name + ' 进入'
    c.wait()
    print threading.current_thread().name + ' 离开'
    c.release()


condition = threading.Condition()
for i in xrange(5):
    t = threading.Thread(target=worker, args=(condition,))
    t.setName('线程 ' + str(i))
    t.start()

time.sleep(3)
condition.acquire()
condition.notify(2)
condition.release()
time.sleep(3)
condition.acquire()
condition.notify(2)
condition.release()
time.sleep(3)
condition.acquire()
condition.notify()
condition.release()
