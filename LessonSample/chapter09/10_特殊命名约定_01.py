#!/usr/bin/python
# -*- coding: UTF-8 -*-


class WebInfo:
    """
    以单下划线开头的表示的是保护类型(protected) 的变量，
    即保护类型只能允许其本身与子类进行访问，
    不能用于 from module import *
    """
    _site = "www.163.com"

    def __init__(self):
        self._site = 'www.apache.org'

# 实际上根本起不到保护作用，仅仅是约定而已，访不访问靠自身觉悟 ^_^！
print WebInfo._site
webinfo = WebInfo()
print webinfo._site
