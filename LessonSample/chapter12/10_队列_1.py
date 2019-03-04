#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
"""仔细观察，会出现重复数据"""
a_list = [x for x in xrange(1000)]


def func01():
    while True:
        try:
            print a_list.pop()
        except:
            break


for i in xrange(3):
    threading.Thread(target=func01).start()
