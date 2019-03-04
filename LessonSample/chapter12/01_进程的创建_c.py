#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from multiprocessing import Process


class ChildProcess(Process):
    def run(self):  # 重写run方法
        print("子进程---%d---%d---" % (os.getpid(), os.getppid()))


p = ChildProcess()
p.start()  # 开启进程

print("主进程---%d---%d---" % (os.getpid(), os.getppid()))
