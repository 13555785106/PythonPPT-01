#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 递归函数,斐波那契数第n个元素值
def fib_seq_val(n):
    if n == 0 or n == 1:
        return 1
    return fib_seq_val(n - 1) + fib_seq_val(n - 2)

print fib_seq_val(40)
