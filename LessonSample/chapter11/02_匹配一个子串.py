#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
#re.search 扫描整个字符串并返回第一个成功的匹配。
print '------------不分组------------'
reg_str = r'[0-9]+'
line = 'www.163.com'
m = re.search(reg_str, line)

print m.span(), m.group()
print m.start()
print m.end()

print '------------分组------------'

reg_str = r'([a-zA-Z]*) are ([a-zA-Z]*?) [a-zA-Z]*'
line = """0123456789 Cats are smarter 
than dogs 0123456789"""
m = re.search(reg_str, line, line, re.M | re.I | re.S)

if m:
    print "m.group() : ", m.group()
    print "m.group(1) : ", m.group(1)
    print "m.group(2) : ", m.group(2)
else:
    print "No match!!"

print '------------带名称的分组------------'
reg_str = r"(?P<first_name>[a-zA-Z]+) (?P<last_name>[a-zA-Z]+)"
line = "0123456789 Malcolm Reynolds 0123456789"
m = re.search(reg_str, line)
print m.groupdict()
