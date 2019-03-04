#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def func01():
    print("...文件...")

menubar = Menu(root)
# 顶级菜单的创建
menubar.add_command(label="文件", command=func01)
menubar.add_command(label="退出", command=root.quit)

root.config(menu=menubar)

root.mainloop()
