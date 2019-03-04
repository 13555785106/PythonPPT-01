#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

def change():
    print(var.get())

root = Tk()
var = IntVar(0)

languages = ["Python", "JavaScript", "Java", "C#"]

labelFrame = LabelFrame(root, text="选择喜欢的语言", padx=5, pady=5)
labelFrame.pack(padx=10, pady=10)
for key, val in enumerate(languages):
    Radiobutton(labelFrame, text=val, variable=var, value=key, command=change).pack(anchor=W)

root.mainloop()
