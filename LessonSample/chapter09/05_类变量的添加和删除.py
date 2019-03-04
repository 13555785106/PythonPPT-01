#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Foo:
    pass

Foo.var1 = '变量1'  # 在类声明之后，可添加类变量
print Foo.var1
del Foo.var1  # 删除类变量
print Foo.var1  # 此行代码会出错，因为类变量var1已经被删除了
