#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 本例演示多继承
class A1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print 'A1.print_name', self.name

class A2:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_name(self):
        print 'A2.print_name', self.name

    def print_sex(self):
        print 'A2.print_sex', self.sex

class B(A1, A2):
    def __init__(self):
        """
        子类如果需要调用多个父类的构造函数的时候，
        存在重复调用的问题。
        """
        A1.__init__(self, 'Tom', 56)
        A2.__init__(self, 'John', 78, '男')

    def print_age(self):
        print 'B.print_age', self.age

b = B()
# 多个父类拥有同名函数，左侧深度优先
b.print_name()

b.print_age()
b.print_sex()

print isinstance(b, B)
print isinstance(b, A1)
print isinstance(b, A2)
