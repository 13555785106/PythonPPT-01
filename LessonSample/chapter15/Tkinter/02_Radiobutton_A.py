#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

def change():
    print(var.get())

root = Tk()

var = IntVar()

Radiobutton(root, text="壹", variable=var, value=1, command=change).pack(anchor=W)
Radiobutton(root, text="贰", variable=var, value=2, command=change).pack(anchor=W)
Radiobutton(root, text="叁", variable=var, value=3, command=change).pack(anchor=W)

root.mainloop()
