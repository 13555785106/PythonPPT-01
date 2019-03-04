#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()

def printCanvas():
    print("Hello World!")

button = Button(canvas, text="点我呀！", command=printCanvas)

canvas.create_window((0, 0), window=button, anchor=NW)
# 默认组件的优先级高，会覆盖重叠部分
canvas.create_line(0, 0, 200, 200, width=6, dash=(10, 2), fill="#FF9966")

root.mainloop()
