#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 本例演示单继承及方法重写
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print 'A.print_name', self.name


class B(A):
    def __init__(self):
        A.__init__(self, 'Tom', 56)

    def print_name(self):  # 重写了父类的同名方法
        print 'B.print_name', self.name

    def print_age(self):
        print 'B.print_age', self.age


print dir(A)
print dir(B)
b = B()
b.print_name()
b.print_age()
print isinstance(b, B)
print isinstance(b, A)
