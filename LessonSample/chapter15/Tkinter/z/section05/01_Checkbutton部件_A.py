#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

root = Tk()

def var_states():
    print("%d,%d" % (var1.get(), var2.get()))

Label(root, text="你的爱好:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(root, text="篮球", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(root, text="足球", variable=var2).grid(row=2, sticky=W)
Button(root, text='显示', command=var_states).grid(row=3, sticky=W, pady=4)
Button(root, text='退出', command=root.quit).grid(row=4, sticky=W, pady=4)

mainloop()
