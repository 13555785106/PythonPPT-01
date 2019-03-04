#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Foo:
    pass

foo = Foo()
foo.var1 = "变量1"  # 添加变量var1
foo.var2 = "变量2"  # 添加变量var2
print foo.var1
print foo.var2

del foo.var1  # 删除实例中变量var1
print foo.var1  # 此行代码会出错，因为已经被删除了
