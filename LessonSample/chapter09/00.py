#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Foo:
    """Simple Class"""

    def __init__(self):
        self.name = 'Tom'

    def printname(self):
        print self.name


foo = Foo()
print foo.name
foo.printname()


def seq(start):
    while True:
        yield start
        start += 1
