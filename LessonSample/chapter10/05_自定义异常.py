#!/usr/bin/python
# -*- coding: UTF-8 -*-

class MyException(RuntimeError):
    def __init__(self, args):
        self.args = args
        self.message = ''.join(self.args)

    def __str__(self):
        return self.message

try:
    raise MyException("出现了我自己定义的错误!")
except MyException, e:
    print e
