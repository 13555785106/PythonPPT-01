#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

def show_values():
    print (scale1.get(), scale2.get())

root = Tk()
scale1 = Scale(root, from_=0, to=50, tickinterval=8,length=200)
scale1.set(19)
scale1.pack()
scale2 = Scale(root, from_=0, to=100, length=400, tickinterval=10, orient=HORIZONTAL)

scale2.set(23)
scale2.pack()
Button(root, text='Show', command=show_values).pack()

mainloop()
