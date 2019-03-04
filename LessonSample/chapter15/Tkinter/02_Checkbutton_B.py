#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
fruits = ["Apple", 'Banana', 'Peach', 'Orange']
values = []

def change():
    print '---------'
    for val in values:
        print(val.get())

for fruit in fruits:
    values.append(BooleanVar())
    b = Checkbutton(root, text=fruit, variable=values[-1], command=change)  # 使用一个固有变量来记录状态
    b.pack(anchor=W)  # 控件相对主窗口在左边
root.mainloop()
