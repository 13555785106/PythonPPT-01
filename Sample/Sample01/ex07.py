#!/usr/bin/python
# -*- coding: UTF-8 -*-

class P1(object):
    def __init__(self):
        self._name = 'P1'

    def func(self):
        print self._name


class P2(object):
    def __init__(self):
        self._name = 'P2'

    def func(self):
        print self._name


class C(P1, P2):
    pass


c = C()
c.func()
