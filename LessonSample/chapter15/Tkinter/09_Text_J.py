#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

root = Tk()

text = Text(root, width=100, height=20, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT, "gag g efwa h eshhe fawf")

def cusSep(*args):  # 每次调用该函数，就还在该位置插入一个分隔符
    text.edit_separator()

text.bind('<Key>', cusSep)

def undo():
    text.edit_undo()

Button(root, text="撤销", command=undo).pack()

root.mainloop()
