#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkColorChooser

master = Tk()

def callback():
    color = tkColorChooser.askcolor()
    print(color)
    # ((109.42578125, 115.44921875, 211.82421875), '#6d73d3') rgb和16进制值

Button(master, text="请选择颜色", command=callback).pack()

master.mainloop()
