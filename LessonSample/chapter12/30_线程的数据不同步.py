#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread, threading, time, datetime, random

print '主线程开始'

ticket_num = [1000]  # 列表是引用传递

class myThread(threading.Thread):
    def __init__(self, tn):
        threading.Thread.__init__(self)
        self.counter = 0
        self.tn = tn

    def run(self):
        num = random.choice([1, 2, 3, 4, 5])
        while True:
            if self.tn[0] <= 0:
                break
            if num < self.tn[0]:
                self.tn[0] -= num
            else:
                num = self.tn[0]
                self.tn[0] = 0
            self.counter += num;
            time.sleep(0.001)

thread_list = []
for i in xrange(5):
    t = myThread(ticket_num)
    t.setDaemon(True)
    t.setName('线程 ' + str(i))
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()

total = 0
for t in thread_list:
    print  t.counter
    total += t.counter
print total
print '主线程结束'
