#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 1.请问下面构造函数第一个变量名称不是self，是否正确？
class Foo:
    def __init__(me, name):
        me.name = name

# 2.回答下面的问题
class Foo:
    name = 'Tom'

foo = Foo()
foo.name = 'John'
print foo.name  # 输出是什么？
print Foo.name  # 输出是什么？

# 3.回答下面的问题
class Foo:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_sex(self):
        print self.sex

Foo().print_sex()  # 能否正确运行？

# 4.回答下面的问题
class Foo:
    pass

def myinit(self, name):
    self.name = name

Foo.__init__ = myinit

foo = Foo()  # 能否正确运行

# 5.回答下面的问题
class A:
    pass

class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class C(A, B):
    pass

c = C()  # 能否正确运行为什么？

# 6.简单描述静态方法与类方法的区别
