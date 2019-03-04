#!/usr/bin/python
# -*- coding: UTF-8 -*-

# for index in [0, 1, 2, 3, 4]:
#    print index

def seq(start):
    while True:
        yield start
        start += 1

for index in seq(100):
    if index > 110:
        break
    print index

print '---------------------------'

def fib():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a

print '---------------------------'
num = 0
for v in fib():
    if num >= 10:
        break
    print "%-5d%5d" % (num, v)
    num += 1
print '---------------------------'
f = fib()
for num in xrange(10):
    print "%-5d%5d" % (num, f.next())
