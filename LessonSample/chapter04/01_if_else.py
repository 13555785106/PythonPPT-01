#!/usr/bin/python
# -*- coding: UTF-8 -*-

sex = '男'
if sex == '男':
    print '60岁退休'
else:
    print '55岁退休'

age = 60
if age < 1 or age > 150:
    print '无效年龄'
elif age <= 3:
    print '婴儿'
elif age <= 7:
    print '幼儿'
elif age <= 11:
    print '童年'
elif age <= 15:
    print '少年'
elif age <= 25:
    print '青年'
elif age <= 60:
    print '成年'
else:
    print '老年'
