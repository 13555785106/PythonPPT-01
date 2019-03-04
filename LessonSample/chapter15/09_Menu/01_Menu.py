#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def callback():
    print("...Hello World...")

menubar = Menu(root)

# 子菜单
filemenu = Menu(menubar, tearoff=False)  # 设置不可分离，不会在菜单界面显示一条虚线（可分离菜单窗口）
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)

editmenu = Menu(menubar)
editmenu.add_command(label="剪切", command=callback)
editmenu.add_command(label="拷贝", command=callback)
editmenu.add_command(label="复制", command=callback)

# 级联菜单
# 顶级菜单
menubar.add_cascade(label="文件", menu=filemenu)
menubar.add_cascade(label="编辑", menu=editmenu)

# 配置后才能显示
root.config(menu=menubar)

root.mainloop()
