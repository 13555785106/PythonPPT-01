#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)  # 创建绘图区域,默认在主窗口居中
canvas.pack()

line1 = canvas.create_line(0, 0, 200, 100, fill="yellow", width=2)
line2 = canvas.create_line(0, 100, 200, 0, fill="red", dash=(12, 5), width=2)  # dash中元组第一个代表点划线长,第二个代表间隔长度
rect1 = canvas.create_rectangle(50, 25, 150, 75, fill="green", outline='white', width=4)

# canvas.coords(line1, 0, 5, 200, 5)  # 坐标移动，至少4个参数，基本上就是重新绘制这条线
# canvas.delete(line2)  # 删除这条线
# canvas.itemconfig(rect1, fill="red")  # 对某一个创建的图形项目进行配置属性
# canvas.itemconfig(line1, fill="green")

Button(root, text="删除所有", command=lambda x=ALL: canvas.delete(x)).pack()

root.mainloop()
