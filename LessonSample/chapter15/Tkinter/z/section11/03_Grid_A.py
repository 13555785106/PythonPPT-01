#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

root = Tk()

colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
r = 0
for c in colours:

    root.rowconfigure(r, weight=1)
    Label(text=c, relief=RIDGE, width=15).grid(row=r, column=0, sticky="nsew")
    Entry(bg=c, relief=SUNKEN, width=10).grid(row=r, column=1, sticky="nsew")
    r = r + 1

root.mainloop()
