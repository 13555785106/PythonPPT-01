#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# findall(string[, pos[, endpos]]) 在字符串中找到正则表达式所匹配的所有子串，
# 并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# re.finditer(pattern, string, flags=0)
# 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('baidu 123 google 456')
result2 = pattern.findall('bai88dub123google456', 0, 10)

print(result1)
print(result2)

print '------------------------------------'
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print (match.group())
