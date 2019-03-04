#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time

import threadpool

lock = threading.Lock()


def print_fruit_name(string):
    lock.acquire()
    print str(threading.current_thread().ident) + string
    lock.release()
    time.sleep(2)


fruits = ['苹果', '香蕉', '鸭梨', '芒果', '桃子', '樱桃', '黄瓜', '茄子', '桂圆', '荔枝']
start_time = time.time()
pool = threadpool.ThreadPool(2)
requests = threadpool.makeRequests(print_fruit_name, fruits)
[pool.putRequest(req) for req in requests]
pool.wait()
print '%d second' % (time.time() - start_time)
