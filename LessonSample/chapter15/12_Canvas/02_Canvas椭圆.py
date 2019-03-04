#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

canvas_width = 300
canvas_height = 240

root = Tk()

canvas = Canvas(root,
                width=canvas_width,
                height=canvas_height)
canvas.pack()
root.update()
canvas.create_oval(5, 5,
                   canvas.winfo_reqwidth() - 5,
                   canvas.winfo_reqheight() - 5,
                   width=5, fill='red',
                   outline='green')

root.mainloop()
