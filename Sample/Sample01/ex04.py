#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        elif attr =='age':
            return lambda: 25

s = Student()

print s.name
print s.score
print s.age()
print s.score3
