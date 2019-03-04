#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

"""反向引用示例"""
s = 'hello blue go go hello apple apple'
p = re.compile(r'\b(\w+)\b\s+\1\b')  # 这里的'\1'就对应前面的(\w+)

print re.findall(p, s)

p = re.compile(r'\b(?P<word>\w+)\b\s+(?P=word)\b')

for m in re.finditer(p, s):
    print m.groupdict()
