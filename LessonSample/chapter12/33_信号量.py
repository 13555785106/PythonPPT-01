#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import threading

semaphore = threading.Semaphore(2)  # 添加一个计数器

def worker(name):
    semaphore.acquire()  # 计数器获得锁
    print(name)
    time.sleep(5)
    semaphore.release()  # 计数器释放锁

for i in range(10):
    t1 = threading.Thread(target=worker, args=('线程' + str(i),))  # 创建线程
    t1.start()  # 启动线程
