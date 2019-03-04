#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def callback():
    print("---Hello World!---")

menubutton = Menubutton(root, text=">", relief=RAISED)
menubutton.pack()

filenemu = Menu(menubutton, tearoff=False)

# 顶级菜单
filenemu.add_command(label="文件", command=callback)
filenemu.add_command(label="编辑", command=callback)

menubutton.config(menu=filenemu)

root.mainloop()
