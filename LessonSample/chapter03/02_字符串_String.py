#!/usr/bin/python
# -*- coding: UTF-8 -*-
str1 = '012345678901234567890123456789'
str2 = "零壹贰叁肆伍陆柒捌玖零壹贰叁肆伍陆柒捌玖零壹贰叁肆伍陆柒捌玖"
str3 = "0123零壹贰叁"
print type(str1)
print type(str2)
print str1, str2
print len(str1), len(str2), len(str2.decode("UTF-8")), len(str3), len(str3.decode("UTF-8"))
print str1[:9]
print str1[9:]
print str1[9:19]
print str1[-1:]
print str1[-3:-1]
print str2[2:5]
print str2.decode("UTF-8")[2:5].encode("UTF-8")
print str3.decode("UTF-8")[2:].encode("UTF-8")

print type(str3.decode("UTF-8")[2:].encode("UTF-8"))
print type(str3.decode("UTF-8"))
