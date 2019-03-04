#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread, time

lock = thread.allocate_lock()
thread_num = 5
signals = []
for i in xrange(thread_num):
    signals.append(0)

# 为线程定义一个函数
def run(sn):
    count = 0
    while count < 10:
        count += 1
        lock.acquire()
        print thread.get_ident(), time.strftime("%H:%M:%S", time.localtime())
        lock.release()
        time.sleep(1)
    signals[sn] = 1

for i in xrange(thread_num):
    lock.acquire()
    print '线程id=%d' % thread.start_new_thread(run, (i,))
    lock.release()

while not all(signals):
    time.sleep(1)
