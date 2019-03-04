#!/usr/bin/python
# -*- coding: UTF-8 -*-


#定义新式类，只需显示继承 object !!!!!!!!
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError('salary 必须大于等于 0')

emp = Emp('Tom')
print emp.name
print emp.salary
# emp.salary = -9
Emp.staticDisplayInstanceCount()
Emp.classDisplayInstanceCount()

emp.displayEmployee()

print type(Emp)
print type(emp)
print isinstance(emp, Emp)
