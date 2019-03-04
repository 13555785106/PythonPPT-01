#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义了一个三参数的函数，age参数有缺省值，
# 传递时可以忽略。
def print_student_info(name, sex, age=50):
    print 'name=%s,sex=%s,age=%d' % (name, sex, age)

# 按顺序传递参数
print_student_info('Tom', '男', 36)
# 忽略默认参数，只传递前两个参数
print_student_info('Kity', '女')
# 使用具名参数传递,顺序随意
print_student_info(age=36, sex='男', name='Tom')
# 使用字典作为参数
dict_student = {'age': 78, 'sex': '女', 'name': '约翰'}
print_student_info(**dict_student)
