#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释  
num = re.subn(r'#.*$', "", phone)
print "电话号码是: ", num
# 删除非数字(-)的字符串
num = re.subn(r'\D', "", phone)
print "电话号码是 : ", num
