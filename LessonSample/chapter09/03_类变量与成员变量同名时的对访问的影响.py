#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Foo:
    """
    在类变量与成员变量同名的情况下，
    使用实例变量访问时，优先返回成员变量的值。
    """
    site = "www.163.com"

    def __init__(self):
        pass
        self.site = 'www.apache.org'  # 注释此行，看看结果

foo = Foo()
print foo.site
print Foo.site
