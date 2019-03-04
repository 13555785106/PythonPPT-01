#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""使用队列通讯"""

from multiprocessing import Process, Queue

def queue_in(q):
    for i in xrange(10):
        q.put(i)

q = Queue()
p = Process(target=queue_in, args=(q,))
p.start()
for v in xrange(10):
    print q.get()
p.join()
