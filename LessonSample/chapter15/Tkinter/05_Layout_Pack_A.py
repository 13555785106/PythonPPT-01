#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
Button(root, text='A').pack(side=LEFT, expand=NO, fill=Y)
Button(root, text='B').pack(side=TOP, expand=NO, fill=BOTH)
Button(root, text='C').pack(side=RIGHT, expand=NO, fill=NONE)
Button(root, text='D').pack(side=LEFT, expand=NO, fill=Y)
Button(root, text='E').pack(side=TOP, expand=NO, fill=BOTH)
Button(root, text='F').pack(side=BOTTOM, expand=NO)
Button(root, text='G').pack(anchor=SE)
root.mainloop()
