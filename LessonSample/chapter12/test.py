#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Queue import Queue
from threading import Thread
import time

que = Queue()

def task(value):
    global que
    que.put(value)
    # que.put(value)

def task2():
    global que
    res = que.get()
    print(res)
    que.task_done()

t1 = Thread(target=task, args=(10,))
t2 = Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()

que.join()




