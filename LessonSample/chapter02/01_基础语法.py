#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = 100  # 变量的声明
print num
empinfo = "Tom" + \
          " 男" + \
          " 78"
print empinfo

def score_level(score):  # 此处定义了函数，演示了缩进语法
    """函数说明，计算分数等级"""
    if score > 100 or score < 0:
        return '无效分数'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

score = 78  # 定义一个分数
print '你的成绩等级是', score_level(score)

class Foo:
    """这是对类描述的说明"""
    pass

# 以下演示的是单、双、及三引号字符串的声明
str1 = 'abc'
str2 = '''abc
def
'''
str3 = "abc"
str4 = """abc
def
"""
