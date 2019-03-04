#!/usr/bin/python
# -*- coding: UTF-8 -*-
ba = bytearray(256)
for index in xrange(256):
    ba[index] = index

print ba
fo = open("foo.bin", "wb")
fo.write(ba)
fo.close()
