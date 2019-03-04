#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# re.split(pattern, string[, maxsplit=0, flags=0])
# 方法按照能够匹配的子串将字符串分割后返回列表。


line = " apple# apple# apple!"
print re.findall(r'\W+', line)
print re.split(r'\W+', line)  # \W+ 匹配非字母数字及下划线
print re.split(r'\W+', line, 1)  # 分割一次
print re.split(r'(\W+)', line)  # 如果使用了分组符号，那么匹配的字符也会被加入到结果列表中！！！

print re.split('z*', line)  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
