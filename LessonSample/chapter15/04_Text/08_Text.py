#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

root = Tk()

text = Text(root, width=40, height=20, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT, "每次输入一个字符都加入一个分割操作，这样会导致撤销时每次回退一个字符！")

def keyInput(event):
    print dir(event)
    print event.char
    print event.keycode
    text.edit_separator()  # 每次调用该函数，就还在该位置插入一个分隔符

text.bind('<Key>', keyInput)

def undo():
    text.edit_undo()

Button(root, text="撤销", command=undo).pack()

root.mainloop()
