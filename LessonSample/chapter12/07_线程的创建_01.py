#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread
import time

thread_num = 5
signals = []
for i in xrange(thread_num):
    signals.append(0)


# 为线程定义一个函数
def run(sn):
    count = 0
    while count < 5:
        count += 1
        print "[", thread.get_ident(), "]"
        time.sleep(1)
    signals[sn] = 1


for i in xrange(thread_num):
    thread.start_new_thread(run, (i,))

while not all(signals):
    time.sleep(1)
