#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
import tkFileDialog

def callback():
    name = tkFileDialog.askopenfilename()
    print name

errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()
