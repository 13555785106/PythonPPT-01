#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

canvas_width = 500
canvas_height = 150

def paint(event):
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=python_green)

root = Tk()
root.title("随手画")
canvas = Canvas(root,
                width=canvas_width,
                height=canvas_height)
canvas.pack(expand=YES, fill=BOTH)
canvas.bind("<B1-Motion>", paint)
message = Label(root, text="按住鼠标左键划线")
message.pack(side=BOTTOM)

mainloop()