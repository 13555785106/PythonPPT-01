#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread, threading, time, datetime, random

print '主线程开始'

threadLock = threading.Lock()
ticket_num = 9999

# 为线程定义一个函数
def sell_ticket():
    global ticket_num
    num = random.choice([1, 2, 3, 4, 5])
    while True:
        threadLock.acquire()
        if ticket_num == 0:
            threadLock.release()
            break
        if num < ticket_num:
            ticket_num -= num
            print threading.current_thread().name, '卖出', num, '剩余', ticket_num
        else:
            print threading.current_thread().name, '卖出', ticket_num, '剩余', 0
            ticket_num = 0
        threadLock.release()
        time.sleep(0.001)

thread_list = []
for i in xrange(5):
    t = threading.Thread(target=sell_ticket)
    t.setDaemon(True)
    t.setName('线程 ' + str(i))
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()

print '主线程结束'
