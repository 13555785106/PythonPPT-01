#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

master = Tk()

text = Text(master, width=32, height=18, undo=True)
text.pack()

text.insert(INSERT, "请输入文字信息，点击撤销按钮可回退！")

Button(master, text="撤销", command=text.edit_undo).pack()

master.mainloop()
