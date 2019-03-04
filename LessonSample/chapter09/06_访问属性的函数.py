#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Emp:
    """所有员工的基类"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "%-10s%-10s%-10s%-10.2f" % ('Name:', self.name, 'Salary:', self.salary)

emp00 = Emp('巫妖王', 1000)
print hasattr(emp00, "name")  # 判断实例中是否存在名称为 name 的属性
print getattr(emp00, "name")  # 无默认参数获取，如果属性不存在抛出异常

setattr(emp00, 'name', '耐奥祖')  # 设置 name 属性，如果不存在则添加
print getattr(emp00, "name")

print hasattr(emp00, "sex")
print getattr(emp00, "sex", "男")  # 带默认参数获取，如果属性不存在不抛异常返回默认值

setattr(emp00, 'sex', '男兽人')  # 此处添加 sex 属性
del emp00.sex  # 此处删除 sex 属性
