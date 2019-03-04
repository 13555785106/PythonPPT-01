#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

options = [
    "苹果",
    "香蕉",
    "桃子",
]

root = Tk()

var = StringVar()
var.set(options[0])

# def __init__(self, master, variable, value, *values, **kwargs):
# w = OptionMenu(master,v,OPTION)
# 不加星号，进行解包，那么只能看做value被输出

# 加星号，列表被序列解包，正常输出*values
optionMenu = OptionMenu(root, var, *options)

optionMenu.pack()

root.mainloop()
