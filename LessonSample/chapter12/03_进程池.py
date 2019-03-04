#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import random
import time
from multiprocessing import Pool


def run(name):
    print("子进程%d启动--%s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.choice([5, 7, 9]))
    end = time.time()
    print("子进程%d结束--%s--耗时%.2f" % (name, os.getpid(), end - start))



print("父进程启动")
# 创建多个进程
# 进程池
# 表示可以同时执行的进程数量
# Pool默认大小是CPU核心数
pp = Pool()
for i in range(10):
    # 创建进程,放入进程池中统一管理
    pp.apply_async(run, args=(i,))
# 在调用join之前必须先调用close,并且调用close之后就不能再继续添加新的进程了
pp.close()  # close以后进程池pp将被关闭,不能再继续向pp中加入新的进程.
# 进程池对象调用join,会等待进程池中所有的子进程结束完毕再去执行父进程
pp.join()
print("父进程结束")
