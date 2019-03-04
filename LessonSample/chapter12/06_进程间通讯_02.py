#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""使用管道通讯"""

from multiprocessing import Process, Pipe


def func01(conn):
    conn.send('Hello World from child process')
    print "子线程输出:"+conn.recv()


parent_conn, child_conn = Pipe()
p = Process(target=func01, args=(child_conn,))
p.start()
print "父线程输出:"+parent_conn.recv()
parent_conn.send('Hello World from parent process')
p.join()
