#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *



def callback(v):
    print v


options = [
    "苹果",
    "香蕉",
    "桃子",
]
root = Tk()
var = StringVar()
var.set(options[1])
optionMenu = OptionMenu(root, var, *options, command=callback)

optionMenu.pack()

root.mainloop()
