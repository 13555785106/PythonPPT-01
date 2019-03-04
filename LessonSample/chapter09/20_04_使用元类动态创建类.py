#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 通过元类动态创建类


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """返回一个类对象，将属性都转为大写形式"""
    print future_class_name
    print future_class_parents
    print future_class_attr
    # 选择所有不以下划线'_'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('_'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过'type'来做类对象的创建并返回
    return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrs:
    __metaclass__ = upper_attr
    name = '肖俊峰'


print hasattr(UpperAttrs, 'name')
# 输出: False
print hasattr(UpperAttrs, 'NAME')
# 输出:True

ua = UpperAttrs()
print ua.NAME
# 输出:'bip'
