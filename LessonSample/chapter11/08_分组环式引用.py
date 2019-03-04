#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

"""环视引用"""
line = 'Hello, Mr.Gumby : 2016/10/26  Hello,r.Gumby : 2016/10/26'

# 不加环视限定
print re.compile("(?P<name>\w+\.\w+)").findall(line)

# 逆序肯定,环视表达式所在位置 左边为 "Hello, "
print re.compile("(?<=Hello, )(?P<name>\w+\.\w+)").findall(line)

# 逆序否定,环视表达式所在位置 左边不为 ","
print re.compile("(?<!,)(?P<name>\w+\.\w+)").findall(line)

# 正序肯定,环视表达式所在位置 右边为 "M"
print re.compile("(?=M)(?P<name>\w+\.\w+)").findall(line)

# 正序否定,环视表达式所在位置 右边不为 r
print re.compile("(?!r)(?P<name>\w+\.\w+)").findall(line)

line = '<div><img src="http://www.baidu.com/img/a.jpg"/><img src="http://www.badu.com/ll/a.jpg"/></div>'

print re.findall(r'(?<=<img src=")[^"]*', line, re.I)
