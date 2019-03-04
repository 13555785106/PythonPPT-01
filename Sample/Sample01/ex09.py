#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

class Student(object):
    '学生类'

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __str__(self):
        return '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('分数必须在0-100之间')


s1 = Student('Bart Simpson', 59)
s2 = Student('Lisa Simpson', 87)
print s1
s2.set_score(100)
s2._Student__score = 900
print s2
