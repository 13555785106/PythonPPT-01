#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

def change():
    print(var.get())

root = Tk()
var = IntVar()

languages = [
    ("Python", 1),
    ("JavaScript", 2),
    ("Java", 3),
    ("C#", 4)
]

labelFrame = LabelFrame(root, text="选择喜欢的语言", padx=5, pady=5)
labelFrame.pack(padx=10, pady=10)
for key, val in languages:
    Radiobutton(labelFrame, text=key, variable=var, value=val, command=change).pack(anchor=W)

root.mainloop()
