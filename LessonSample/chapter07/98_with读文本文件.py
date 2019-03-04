#!/usr/bin/python
# -*- coding: UTF-8 -*-

with open("foo.txt", "r") as fo:
    raise Exception("抛出一个异常")
    print fo.read()

print '---------'
