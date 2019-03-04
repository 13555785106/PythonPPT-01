#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Emp(object):
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary=9999.99):
        self.name = name
        self.salary = salary
        self.__class__.empCount += 1

    @staticmethod  # 静态方法
    def staticDisplayInstanceCount():
        print '静态方法'
        print "Total Employee %d" % Emp.empCount

    @classmethod  # 类方法
    def classDisplayInstanceCount(cls):
        print '类方法'
        print "Total Employee %d" % cls.empCount

    def displayEmployee(self):
        print "Name : ", self.__name, ", Salary: ", self.__salary

print '---------以下是内置类属性---------'
print Emp.__name__  # 类名
print Emp.__doc__  # 类说明
print Emp.__module__  # 模块名
print Emp.__dict__  # 类中的成员
print Emp.__bases__  # 父类
