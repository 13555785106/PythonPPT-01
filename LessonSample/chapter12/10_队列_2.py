#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue
import threading
import time

# 队列本身是线程安全的，其内部已经实现了数据同步。


consumer_num = 10
queue = Queue.Queue()


def consumer():
    while True:
        val = queue.get()
        if val == -1:
            break
        else:
            print val


def producer():
    num = 0
    while num < 100:
        queue.put(num)
        num += 1
        time.sleep(0.001)
    else:
        for v in xrange(consumer_num):
            queue.put(-1)


threading.Thread(target=producer).start()

for i in xrange(consumer_num):
    threading.Thread(target=consumer).start()
