#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox

root = Tk()
text = Text(root, width=32, height=6, font=("Times", "16", "bold italic"))
text.pack()
paragraph = '''012345678901234567890123456789
012345678901234567890123456789
012345678901234567890123456789'''
text.insert(CURRENT, paragraph)

positions = ("1.7", "1.12", "1.16")

text.tag_add("href", *positions)
text.tag_config("href", background="yellow", foreground="red", underline=True,
                font=("Times", "20", "bold italic"))

def show_arrow_cursor(*args):
    text.config(cursor="arrow")  # 箭头

def show_xterm_cursor(*args):
    text.config(cursor="xterm")  # 光标线

def click(*args):
    line = ''
    length = len(positions)
    for i in xrange(0, length, 2):
        if i + 1 < length:
            line += text.get(positions[i], positions[i + 1])
        else:
            line += text.get(positions[i])
        line += ' '
    tkMessageBox.showinfo('提示', line)

text.tag_bind("href", "<Enter>", show_arrow_cursor)
text.tag_bind("href", "<Leave>", show_xterm_cursor)
text.tag_bind("href", "<Button-1>", click)

root.mainloop()
