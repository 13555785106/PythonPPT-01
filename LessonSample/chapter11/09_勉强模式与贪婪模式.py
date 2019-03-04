#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

line = 'xfooxxxxxxfooxxxxxxfoo'
print '---------贪婪模式结果---------'
reg_str = r'.*foo'
m = re.search(reg_str, line)
print m.span(), m.group()
print '---------勉强模式结果---------'
reg_str = r'.*?foo'
m = re.search(reg_str, line)
print m.span(), m.group()

