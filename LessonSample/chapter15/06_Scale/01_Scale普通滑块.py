#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

scale01 = Scale(root, from_=0, to=42)  # 默认是垂直的
scale01.pack()

scale02 = Scale(root, from_=0, to=200, orient=HORIZONTAL)  # 设置为水平
scale02.pack()

def printValue():
    print scale01.get(), scale02.get()

Button(root, text="打印数值", command=printValue).pack()

root.mainloop()
