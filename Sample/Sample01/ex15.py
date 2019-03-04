#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

s = 'Hello, Mr.Gumby : 2016/10/26  Hello,r.Gumby : 2016/10/26'
#print re.compile("(?P<name>\w+\.\w+)").findall(s)

# 环视表达式所在位置 左边为 "Hello, "
#print re.compile("(?<=Hello,)(?P<name>\w+\.\w+)").findall(s)
# output> ['Mr.Gumby']

# 环视表达式所在位置 左边不为 ","
#print re.compile("(?<!,)(?P<name>\w+\.\w+)").findall(s)
# output> ['Mr.Gumby']

# 环视表达式所在位置 右边为 "M"
print re.compile("(?=M)(?P<name>\w+\.\w+)").findall(s)
print re.search("(?=M)(?P<name>\w+\.\w+)",s).group()

# output> ['Mr.Gumby']

# 环视表达式所在位置 右边不为 r
print re.compile("(?!r)(?P<name>\w+\.\w+)").findall(s)
# output> ['Mr.Gumby']
