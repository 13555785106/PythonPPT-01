#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ctypes import *
hw = CDLL('./CHelloWorld.dll')
print hw.sum(4,5)
hw.sayHello(u'Tom汤姆'.encode('UTF8'))

