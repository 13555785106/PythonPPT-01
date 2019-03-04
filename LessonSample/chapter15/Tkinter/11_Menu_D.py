#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

menubar = Menu(root)

openvar = StringVar()
savevar = StringVar()
quitvar = StringVar()
editvar = StringVar()

def callback():
    print("---Hello World!---")
    print editvar.get()

# 子菜单
filemenu = Menu(menubar, tearoff=False)  # 设置不可分离，不会在菜单界面显示一条虚线（可分离菜单窗口）
filemenu.add_checkbutton(label="打开", command=callback, variable=openvar)
filemenu.add_checkbutton(label="保存", command=callback, variable=savevar)
filemenu.add_separator()
filemenu.add_checkbutton(label="退出", command=root.quit, variable=quitvar)

editmenu = Menu(menubar)
editmenu.add_radiobutton(label="剪切", command=callback, variable=editvar)
editmenu.add_radiobutton(label="拷贝", command=callback, variable=editvar)
editmenu.add_radiobutton(label="复制", command=callback, variable=editvar)

# 级联菜单
# 顶级菜单
menubar.add_cascade(label="文件", menu=filemenu)
menubar.add_cascade(label="编辑", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
