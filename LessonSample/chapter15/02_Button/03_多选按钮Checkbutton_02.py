#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
fruits = ["苹果", '香蕉', '桃子', '橙子', '猕猴桃']
vals = []

def change():
    print str([x.get() for x in vals if x.get()]).decode("unicode-escape")

for fruit in fruits:
    # 使用一个固有变量来记录状态
    vals.append(StringVar())
    b = Checkbutton(root, text=fruit, variable=vals[-1], onvalue=fruit, offvalue='', command=change)
    b.pack(anchor=W)  # 控件相对主窗口在左边
root.mainloop()
