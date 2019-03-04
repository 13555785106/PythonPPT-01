#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=48, height=24)
text.pack()
paragraph='''0123456789012345678901234567890123456789
0123456789012345678901234567890123456789
0123456789012345678901234567890123456789
0123456789012345678901234567890123456789
0123456789012345678901234567890123456789
'''
text.insert(CURRENT, paragraph)
# 注意行数是从1开始，列数是从0开始，
# 索引写法可以使用小数点连接：1.2---第一行第3列
# 特殊：行.end（该行最后的索引）,特殊的需要使用引号
# """Return the text from INDEX1 to INDEX2 (not included)."""
txt = text.get(1.2, '1.end')
txt2 = text.get(2.3, 2.9)
print(txt, txt2)  #

root.mainloop()
