#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

def show_values():
    print (scale1.get(), scale2.get())

root = Tk()
scale1 = Scale(root, from_=0, to=50)
scale1.set(10)
scale1.pack()
scale2 = Scale(root, from_=0, to=200, orient=HORIZONTAL)
scale2.set(150)
scale2.pack()
Button(root, text='Show', command=show_values).pack()

mainloop()
