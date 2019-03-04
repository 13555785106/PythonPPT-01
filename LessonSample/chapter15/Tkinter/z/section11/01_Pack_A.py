#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

root = Tk()

w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=BOTH, expand=1, padx=10, pady=10, ipadx=10, ipady=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=BOTH, expand=1)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=BOTH, expand=1,ipadx=0, ipady=0)

mainloop()
