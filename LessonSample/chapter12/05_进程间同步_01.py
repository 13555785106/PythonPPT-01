#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Process, Lock

'''未同步'''


def func():
    for x in xrange(100):
        print 'Hello World'


lock = Lock()
pList = []
for num in range(100):
    pList.append(Process(target=func))
for p in pList:
    p.start()
