#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def callback(event):
    print dir(event)
    print "x=%d,y=%d" % (event.x, event.y)

frame = Frame(root, width=200, height=200)
frame.pack()
# 绑定事件
frame.bind("<Button-1>", callback)  # 鼠标左键
frame.bind("<Button-2>", callback)  # 鼠标滚轮
frame.bind("<Button-3>", callback)  # 鼠标右键

root.mainloop()
