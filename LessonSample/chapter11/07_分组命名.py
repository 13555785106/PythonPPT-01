#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

"""分组命名示例"""
s = 'age:13,name:Tom;age:18,name:John'
p = re.compile(r'age:(?P<age>\d+),name:(?P<name>\w+)')
it = re.finditer(p, s)
for m in it:
    print type(m), m.groupdict()

for v in re.findall(p, s):
    print v
