#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Process
from time import sleep

def run():
    print("子进程启动")
    sleep(5)
    print("子进程结束")

if __name__ == "__main__":
    print("父进程启动")
    p = Process(target=run)
    p.start()
    # 父进程的结束不能影响子进程,让父进程等待子进程结束,再执行父进程
    p.join()  # 让父进程阻塞在这里, 等待子进程结束后再执行以下语句
    print("父进程结束")
