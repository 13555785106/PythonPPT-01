#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print '------------不分组------------'
reg_str = r'w+'
line = 'www.163.com'
m = re.match(reg_str, line)

print m.span(), m.group()
print m.start()
print m.end()

print '------------分组------------'

reg_str = r'([a-zA-Z]*) are ([a-zA-Z]*?) [a-zA-Z]*'
line = """Cats are smarter 
than dogs"""
m = re.match(reg_str, line, re.M | re.I | re.S)

if m:
    print "m.group() : ", m.group()
    print "m.group(1) : ", m.group(1)
    print "m.group(2) : ", m.group(2)
else:
    print "No match!!"

print '------------带名称的分组------------'
reg_str = r"(?P<first_name>[a-zA-Z]+) (?P<last_name>[a-zA-Z]+)"
line = "Malcolm Reynolds"
m = re.match(reg_str, line)
print m.groupdict()
