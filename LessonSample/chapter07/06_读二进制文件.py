#!/usr/bin/python
# -*- coding: UTF-8 -*-

fo = open("foo.bin", "rb")
ba = bytearray(fo.read())
fo.close()
for v in ba:
    print v
