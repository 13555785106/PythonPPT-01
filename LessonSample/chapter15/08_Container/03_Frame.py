#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
# 以不同的颜色区别各个frame
for color in ['red', 'blue', 'yellow', 'green', 'white', 'black']:
    frame = Frame(root, height=20, width=400, bg=color)
    Label(frame, justify=CENTER, text=color).pack(side=TOP)
    frame.pack(ipadx=10, ipady=10,fill=BOTH,expand=1)

root.mainloop()
