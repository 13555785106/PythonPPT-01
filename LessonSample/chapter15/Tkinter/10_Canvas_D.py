#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

import math

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

center_x = 100
center_y = 50
radius = 50

points = [
    # 左上点
    center_x - int(radius * math.sin(2 * math.pi / 5)),
    center_y - int(radius * math.cos(2 * math.pi / 5)),
    # 右上点
    center_x + int(radius * math.sin(2 * math.pi / 5)),
    center_y - int(radius * math.cos(2 * math.pi / 5)),
    # 左下角
    center_x - int(radius * math.sin(math.pi / 5)),
    center_y + int(radius * math.cos(math.pi / 5)),
    # 顶点
    center_x,
    center_y - radius,
    # 右下角
    center_x + int(radius * math.sin(math.pi / 5)),
    center_y + int(radius * math.cos(math.pi / 5)),
]

print(points)

canvas.create_polygon(points, fill="green", outline="white", width=4)  # 轮廓线

root.mainloop()
