#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 定义函数
def mye(level):
    if level < 1:
        raise ValueError, "Invalid level!必须大于等于1"
        # 触发异常后，后面的代码就不会再执行

try:
    mye(0)  # 触发异常
except ValueError, err:
    print err
else:
    print '成功运行'
