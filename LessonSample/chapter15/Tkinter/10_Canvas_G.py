#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
canvas = Canvas(root, width=200, height=200)
canvas.pack()
root.update()
print canvas.winfo_width(), canvas.winfo_height()
photoImage = PhotoImage(file="python.gif")
canvas.create_image((canvas.winfo_width()/2, canvas.winfo_height()/2), image=photoImage)

root.mainloop()
