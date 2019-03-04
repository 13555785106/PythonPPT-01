#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
master = Tk()
canvas = Canvas(master, width=320, height=240, bg='white')
canvas.pack(fill=BOTH, expand=1, padx=5, pady=5)

def configure(event):
    canvas.delete("all")
    print canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    print event.width, event.height
    canvas.create_rectangle(0, 0, event.width, event.height, fill='black', outline='purple', stipple='gray12')

    for x in range(20, event.width, 20):
        canvas.create_line(x, 0, x, event.height, fill="#476042")
    for y in range(20, event.height, 20):
        canvas.create_line(0, y, event.width, y, fill="#476042")

canvas.bind("<Configure>", configure)
mainloop()
