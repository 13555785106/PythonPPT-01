#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 动态创建类
@classmethod  # 类方法
def test_class_method_a(cls):
    print("test_class_method_a被调用")
    print(cls)


@staticmethod  # 静态方法
def test_static_method_a():
    print("test_static_method_a被调用")


def print_name_a(self):
    print("print_name_a被调用")
    print(self.name)


A = type("A", (),
         {'name': 'Tom_A',
          'test_class_method': test_class_method_a,
          'test_static_method': test_static_method_a,
          'print_name': print_name_a})

A.test_static_method()  # 静态方法可通过类名直接调用
A.test_class_method()  # 类方法可通过类名直接调用
# A.print_name() 成员函数不能通过类名调用，取消此注释会出错
print A.name  # 输出类变量
a = A()
print a.name  # 其实a这个实例中没有name属性，所以返回的是类里的name属性
a.name = 'John'  # 此行代码等于直接向a实例中添加了一个属性name
print a.name  # 实例中的name属性
print A.name  # 类中的name属性
a.print_name()
print '---------------------------'


@classmethod  # 类方法
def test_class_method_b(cls):
    print("test_class_method_b被调用")
    print(cls)


@staticmethod  # 静态方法
def test_static_method_b():
    print("test_static_method_b被调用")


def print_name_b(self):
    print("print_name_b被调用")
    print(self.name)


B = type("B", (A,), {'name': 'Tom_B',
                     'test_class_method': test_class_method_b,
                     'test_static_method': test_static_method_b,
                     'print_name': print_name_b})
B.test_static_method()
B.test_class_method()
# B.print_name() 成员函数不能通过类名调用，取消此注释会出错
print B.name
b = B()
print b.name
b.name = 'John'
print b.name
print B.name
b.print_name()
print '---------------------------'

print type(A)
print type(a)
print type(B)
print type(b)
