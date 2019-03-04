#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

scale01 = Scale(root, from_=0, to=42, tickinterval=5)  # tickinterval是设置分为几份
scale01.pack()

scale02 = Scale(root, from_=0, to=200, orient=HORIZONTAL, resolution=10)  # resolution设置每次移动的固定步长
scale02.pack()

def printValue():
    print scale01.get(), scale02.get()

Button(root, text="获取数值", command=printValue).pack()

root.mainloop()
