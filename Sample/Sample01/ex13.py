#!/usr/bin/python
# -*- coding: UTF-8 -*-


class A1(object):
    def __init__(self):
        super(A1, self).__init__()
        self.var1 = 100
        self.n = 90
        print 'A1 init'

    def minus(self, m):
        print 'A1 minus'
        self.n -= m


class A2(object):
    def __init__(self):
        super(A2, self).__init__()
        self.var2 = 400
        self.n = 100
        print 'A2 init'

    def minus(self, m):
        print 'A2 minus'
        self.n -= m


class D(A1, A2):
    def __init__(self):
        super(D, self).__init__()

    def minus(self, m):
        print 'D minus'
        super(D, self).minus(m)
        self.n -= 2


print D.__mro__
d = D()
print d.n
d.minus(2)
print d.n
print d.var1
print d.var2
