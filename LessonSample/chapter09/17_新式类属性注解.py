#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    @property
    def size(self, size):
        return self.width, self.height

    @size.setter
    def size(self, size):
        self.width, self.height = size

r = Rectangle()
r.size = 200, 100
print r.width

print type(Rectangle)
print type(r)
