#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# re.sub(pattern, repl, string, count=0, flags=0)
# 用于替换字符串中的匹配项。

# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

phone = "024-888666222 # 这是一个固定电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是 : ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num

# 将匹配的数字乘以 2
def double(matched):
    print type(matched)
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
