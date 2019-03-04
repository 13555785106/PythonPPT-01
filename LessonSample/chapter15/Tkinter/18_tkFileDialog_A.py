#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFileDialog

master = Tk()

def callback():
    filename = tkFileDialog.askopenfilename(filetypes=[("PNG", ".png"), ("GIF", ".gif"), ("JPG", ".jpg")])
    print(filename)

Button(master, text="open file", command=callback).pack()

master.mainloop()
