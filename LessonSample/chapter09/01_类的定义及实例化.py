#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

# 此类仅仅是添加了两个成员函数
class Ellipse:
    """定义一个椭圆"""

    def __init__(self, major_radius, minor_radius):
        """构造函数,第一个参数代表实例本身，约定使用参数名为self"""
        self.major_radius = major_radius  # 添加一个成员变量并赋值
        self.minor_radius = minor_radius  # 同上

    # 以下成员函数，必须有一个参数，第一个参数代表实例本身，约定使用self
    def area(self):
        """求面积的成员函数"""
        return math.pi * self.major_radius * self.minor_radius

    def perimeter(self):
        """求周长的成员函数"""
        a = self.major_radius
        b = self.minor_radius
        if a < b:
            b = self.major_radius
            a = self.minor_radius

        return 2 * math.pi + 4 * (a - b)

    def __str__(self):
        """以字符串形式返回实例的描述信息"""
        return "%s%f,%s%f" % ('majorRadius=', self.major_radius, 'minorRadius=', self.minor_radius)

ellipse01 = Ellipse(4, 5)  # 创建一个Ellipse实例
print ellipse01.area()  # 调用成员函数
ellipse01.major_radius = 40  # 修改属性
ellipse01.minor_radius = 50
print ellipse01.area()
