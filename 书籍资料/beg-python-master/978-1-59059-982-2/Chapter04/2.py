# -*- coding:utf-8 -*-
from math import sqrt

for x in range(99, 0, -1):
    root = sqrt(x)
    if (root == int(root)):
        print x
        break
