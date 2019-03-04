#!/usr/bin/python
# -*- coding: UTF-8 -*-
def fn1(self, name='Hello'):  # 先定义函数
    print('Hello, %s.' % name)


def fn2(self, name='World'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(fn1=fn1, fn2=fn2))  # 创建Hello class
h = Hello()
h.fn1()
h.fn2()
