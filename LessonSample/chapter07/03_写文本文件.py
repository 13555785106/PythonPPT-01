#!/usr/bin/python
# -*- coding: UTF-8 -*-
multi_line = '''
apple 苹果鸭梨
牛羊肉

Hello World!
程序人生
'''
fo = open("foo.txt", "w")
fo.write(multi_line)
fo.close()
