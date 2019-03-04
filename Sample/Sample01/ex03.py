#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self,age):
        print('My name is %s %d.' % (self.name,age))


s = Student('Michael')
s(44)
