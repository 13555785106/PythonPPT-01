#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

for fruit in ['apple', 'banana', 'orange']:
    print fruit

fruits = ['apple', 'banana', 'orange']
for index in range(len(fruits)):
    print index, fruits[index]
for c in 'apple':
    print c

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print num, '是一个质数'

def is_prime(num):
    sqrt = int(math.sqrt(num))
    i = 2
    while i <= sqrt:
        if num % i == 0:
            break
        i += 1
    if i > sqrt:
        return True
    else:
        return False

print is_prime(31)
