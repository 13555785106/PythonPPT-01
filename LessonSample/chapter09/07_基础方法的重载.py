#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Emp:
    """所有员工的基类"""

    def __init__(self, name, salary):
        """构造方法"""
        self.name = name
        self.salary = salary

    def __str__(self):
        """提供实例的描述信息"""
        return "%-10s%-10s%-10s%-10.2f" % ('Name:', self.name, 'Salary:', self.salary)

    def __repr__(self):
        """转化为供解释器读取的形式"""
        return "{'name': self.name, 'salary': self.salary}"

    def __cmp__(self, other):
        """比较函数"""
        ret = cmp(self.name, other.name)
        if ret != 0:
            return ret
        else:
            return cmp(self.salary, other.salary)

    def __del__(self):
        """析构函数，实例被销毁时调用"""
        print  self.name, '被删除'

emp00 = Emp('巫妖王', 1000)  # 调用的是 __init__构造函数

print emp00  # 此处默认调用 emp00.__str__函数

emp00Dict = repr(emp00)  # 此处调用 emp00__repr__
print emp00Dict

emp01 = Emp('Tom', 88)
print emp01
emp02 = Emp('John', 55)
print emp02
print cmp(emp01, emp02)  # 此处调用 __cmp__函数
