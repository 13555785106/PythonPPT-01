#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

# 向前肯定断言的语法：(?=pattern) 
print re.sub(r're(?=gular)', 'U', 'a regular expression')
# 向前否定断言语法：(?!pattern) 
print re.sub(r're(?!gular)', 'U', 'a regular expression')
# 向后肯定断言的语法：(?<=pattern) 
print re.sub(r'(?<=\w)re', 'U', 'regex represents regular expression')
# 向后否定断言语法：(?<!pattern)
print re.sub(r'(?<!\w)re', 'U', 'regex represents regular expression')

code_str = '''
 char *a="hello world"; 
char b='c';
/* this is comment */
 int c=1;
/* this is multi-
-line comment
*/ 
'''
# +? 勉强模式的一次或多次
print re.findall(r'(?<=/\*).+?(?=\*/)', code_str, re.M | re.S)
