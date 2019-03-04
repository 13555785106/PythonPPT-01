#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Process, Semaphore

'''使用信号量同步'''


def func(s):
    for x in xrange(10):
        try:
            s.acquire()
            print 'Hello World'
        finally:
            s.release()


s = Semaphore(1)
pList = []
for num in range(100):
    pList.append(Process(target=func, args=(s,)))
for p in pList:
    p.start()
