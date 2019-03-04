#!/usr/bin/python
# -*- coding: UTF-8 -*-

class A(object):
    def __enter__(self):
        print '__enter__'
        return self

    def func(self):
        print 'func 执行'

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print '__exit__'
        print exc_type, exc_value, exc_traceback
        return False


with A() as a:
    1 / 0
    a.func()

print '结束'
