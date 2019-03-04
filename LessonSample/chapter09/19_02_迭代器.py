#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

fibs = Fibs()
print fibs.next()
print fibs.next()
print fibs.next()
print fibs.next()
