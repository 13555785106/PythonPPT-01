#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

master = Tk()

text = Text(master, width=32, height=18, undo=True)
text.pack()

text.insert(INSERT, "gag g efwa h eshhe fawf")

def undo():
    text.edit_undo()

Button(master, text="撤销", command=undo).pack()

master.mainloop()
