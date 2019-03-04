#!/usr/bin/python
# -*- coding: UTF-8 -*-

import inspect

class D(object): pass

class E(object): pass

class F(object): pass

class B(D, E): pass

class C(E, F): pass

class A(B, C): pass

print inspect.getmro(A)
