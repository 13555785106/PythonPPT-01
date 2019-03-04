#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 本例演示多继承
class A1(object):
    def __init__(self, name='Tom', age=99, sex='男'):
        print "A1构造函数被调用"
        self.name = name
        self.age = age
        self.sex = sex

    def print_name(self):
        print 'A1.print_name', self.name

class A2(object):
    def __init__(self):
        print "A2构造函数被调用"

    def print_name(self):
        print 'A2.print_name', self.name

    def print_sex(self):
        print 'A2.print_sex', self.sex

class B(A1, A2):  # 多个父类拥有同名函数，谁在前面调用谁，当然子类可以覆盖
    def __init__(self):
        super(B, self).__init__()

    def print_age(self):
        print 'B.print_age', self.age

b = B()
b.print_name()
b.print_age()
b.print_sex()
