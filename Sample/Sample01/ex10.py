#!/usr/bin/python
# -*- coding: UTF-8 -*-

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print cls
        print name
        print bases
        print attrs

        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass  # 指示使用ListMetaclass来定制类


L = MyList()
L.add(1)
L.add(2)
L.add(3)

print L
