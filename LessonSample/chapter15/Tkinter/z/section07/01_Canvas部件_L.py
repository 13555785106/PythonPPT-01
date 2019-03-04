#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

# create a canvas with no internal border
canvas = Canvas(bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=1)

# track changes to the canvas size and draw
# a rectangle which fills the visible part of
# the canvas

def configure(event):
    canvas.delete("all")
    w, h = event.width, event.height
    xy = 0, 0, w - 1, h - 1
    canvas.create_rectangle(xy)
    canvas.create_line(xy)
    xy = w - 1, 0, 0, h - 1
    canvas.create_line(xy)

canvas.bind("<Configure>", configure)

mainloop()
