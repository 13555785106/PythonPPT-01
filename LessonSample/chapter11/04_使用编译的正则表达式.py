#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# re.compile(pattern[, flags]) 函数用于编译正则表达式，
# 生成一个正则表达式（ Pattern ）对象，
# 供 match() 和 search() 这两个函数使用。
# pattern : 一个字符串形式的正则表达式
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释


pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print m
print m.group(0)  # 返回匹配成功的整个子串
print m.span(0)  # 返回匹配成功的整个子串的索引
print m.group(1)  # 返回第一个分组匹配成功的子串
print m.span(1)  # 返回第一个分组匹配成功的子串的索引
print m.group(2)  # 返回第二个分组匹配成功的子串
print m.span(2)  # 返回第二个分组匹配成功的子串
print m.groups()  # 等价于 (m.group(1), m.group(2), ...)
print m.group(3)  # 不存在第三个分组,运行到这里会出错！！！！
