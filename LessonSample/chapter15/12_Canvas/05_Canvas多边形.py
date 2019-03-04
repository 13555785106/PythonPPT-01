#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

canvas_width = 200
canvas_height =200
python_green = "#476042"

root = Tk()

canvas = Canvas(root,
                width=canvas_width,
                height=canvas_height)
canvas.pack()

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]

canvas.create_polygon(points, outline=python_green,
                      fill='yellow', width=3)

root.mainloop()
