#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()


canvas.create_rectangle(40, 20, 160, 80, fill="green", dash=(4, 4))
canvas.create_oval(40, 20, 160, 80, fill="pink") #创建椭圆
canvas.create_arc(40, 20, 160, 80, fill="blue", width=3)  #创建扇形需两个点，作为两个端点
canvas.create_polygon(40, 20, 160, 80, 30, 10, 40, 20, fill="white") #绘制多边形，会自动封闭图形(首尾)


root.mainloop()
