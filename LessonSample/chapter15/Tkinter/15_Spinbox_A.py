#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

# sx = Spinbox(master,from_=0,to=10)  #0-10
# sx.pack()

spinbox = Spinbox(root, values=("苹果", "香蕉", "桃子"))
spinbox.pack()

root.mainloop()
