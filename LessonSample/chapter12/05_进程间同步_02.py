#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Process, Lock

'''使用锁同步'''

def func(lock):
    for x in xrange(10):
        try:
            lock.acquire()
            print 'Hello World'
        finally:
            lock.release()

lock = Lock()
pList = []
for num in range(100):
    pList.append(Process(target=func, args=(lock,)))
for p in pList:
    p.start()
