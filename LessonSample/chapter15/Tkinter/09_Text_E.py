#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=32, height=6, font=("Times", "18", "bold italic"))
text.pack()
paragraph = '''012345678901234567890123456789
012345678901234567890123456789
012345678901234567890123456789'''
text.insert(CURRENT, paragraph)

text.tag_add("tag1", "1.7", "1.12", "1.16")  # 索引双数为范围，单数为一个字符
text.tag_config("tag1", background="red", foreground="white")  # config是设置样式 foreground是前景色，字体颜色
# 新样式覆盖旧样式
text.tag_add("tag2", "2.9", "2.12")  # 索引双数为范围，单数为一个字符
text.tag_config("tag2", background="blue", foreground="white")  # config是设置样式 foreground是前景色，字体颜色

# 设置tag的优先级:作用就是较低的优先级样式是无法覆盖高优先级的
text.tag_lower("tag2")  # 降低
# text.tag_raise("tag1")  #提高

root.mainloop()
