#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 定义了一个不限数量参数的函数
def str_join(*args):
    return '-'.join(args)

print str_join('a', 'b')
print str_join('a', 'b', 'c')
# 可以传入一个序列
list_str = ['x', 'y', 'z']
print str_join(*list_str)
