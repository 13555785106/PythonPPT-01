#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=160)
canvas.pack()

def paint(event):  # 事件触发
    x1, y1 = (event.x - 1, event.y - 1)
    x2, y2 = (event.x + 1, event.y + 1)
    canvas.create_oval(x1, y1, x2, y2)

canvas.bind("<B1-Motion>", paint)  # 鼠标左键点击移动
root.mainloop()
