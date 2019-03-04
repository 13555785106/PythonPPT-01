#!/usr/bin/python
# -*- coding: UTF-8 -*-


class NewStyleClassA(object):
    var = 'New Style Class A'


class NewStyleClassB(NewStyleClassA):
    pass


class NewStyleClassC(object):
    var = 'New Style Class C'


class SubNewStyleClass(NewStyleClassB, NewStyleClassC):
    pass


if __name__ == '__main__':
    print(SubNewStyleClass.mro())
    print(SubNewStyleClass.var)