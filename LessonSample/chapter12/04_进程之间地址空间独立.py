#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Process

num_list = [1, ]


def run():
    print("子进程开始")
    # global表示引用全局变量num_list
    global num_list
    num_list.append(3)
    print "子进程的 num_list", num_list


print "父进程开始"
p = Process(target=run)
p.start()
p.join()
num_list.append(2)
print "父进程的 num_list", num_list
