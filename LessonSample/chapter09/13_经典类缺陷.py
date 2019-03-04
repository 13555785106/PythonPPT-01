#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 经典类缺陷
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print 'A.print_name', self.name

class B(A):
    def __init__(self):
        A.__init__(self, 'Tom', 56)

    def print_age(self):
        print 'B.print_age', self.age

b = B()
print type(B)
print type(b)
print type(b.__class__)
