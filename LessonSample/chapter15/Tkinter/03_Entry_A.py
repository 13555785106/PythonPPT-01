#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

input = Entry(root)
input.pack(padx=20, pady=20)

input.delete(0, END)  # 先清空按照索引
input.insert(0, "请输入内容...")

root.mainloop()
