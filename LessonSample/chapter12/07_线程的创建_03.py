#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread
import threading
import time

thread_num = 5
signals = []
for i in xrange(thread_num):
    signals.append(0)


# 为线程定义一个函数
def run(sn):
    for v in xrange(5):
        print "[", thread.get_ident(), "]"
        time.sleep(1)
    signals[sn] = 1


for i in xrange(thread_num):
    t = threading.Thread(target=run, args=(i,))
    t.start()

while not all(signals):
    time.sleep(1)
