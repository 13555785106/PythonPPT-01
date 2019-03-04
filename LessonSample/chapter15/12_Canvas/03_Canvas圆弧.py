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

canvas.create_arc(5, 5,
                  canvas.winfo_reqwidth() - 5,
                  canvas.winfo_reqheight() - 5,
                  start=0, extent=90,
                  width=5, fill='red',
                  outline='green',
                  )
canvas.create_arc(5, 5,
                  canvas.winfo_reqwidth() - 5,
                  canvas.winfo_reqheight() - 5,
                  start=90, extent=90,
                  width=5,
                  outline='green',
                  )
canvas.create_arc(5, 5,
                  canvas.winfo_reqwidth() - 5,
                  canvas.winfo_reqheight() - 5,
                  start=180, extent=90,
                  width=0,
                  fill='blue',
                  outline='blue'
                  )
canvas.create_arc(5, 5,
                  canvas.winfo_reqwidth() - 5,
                  canvas.winfo_reqheight() - 5,
                  start=270, extent=90,
                  width=5,
                  style=ARC
                  )
root.mainloop()
