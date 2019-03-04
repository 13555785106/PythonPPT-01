#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functools import partial as pto

def add(a, b):
    return a + b;

puls = pto(add,100)

print puls(9)
print puls(30)