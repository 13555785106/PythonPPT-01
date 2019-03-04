#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

"""
def checkered(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")
"""
master = Tk()

canvas = Canvas(master, width=320, height=240, bg='white')
canvas.pack(fill=BOTH, expand=1, padx=5, pady=5)

# checkered(w, 10)
def configure(event):
    canvas.delete("all")
    print canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    print event.width, event.height
    canvas.create_rectangle(0, 0, event.width, event.height, fill='black', outline='purple', stipple='gray12')
    # canvas.create_line(0, 3, event.width, 3, fill='#000000')

    for x in range(10, event.width, 10):
        canvas.create_line(x, 0, x, event.height, fill="#476042")
    for y in range(10, event.height, 10):
        canvas.create_line(0, y, event.width, y, fill="#476042")

canvas.bind("<Configure>", configure)
mainloop()
