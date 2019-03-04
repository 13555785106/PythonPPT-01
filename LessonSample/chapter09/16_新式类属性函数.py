#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

r = Rectangle()
r.size = 200, 100
print r.width

print type(Rectangle)
print type(r)
