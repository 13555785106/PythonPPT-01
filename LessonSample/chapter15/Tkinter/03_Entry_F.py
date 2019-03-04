#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

val1 = StringVar()
val2 = StringVar()
valSum = StringVar()

def validateInput(content):
    if content.isdigit():
        return True
    else:
        return False

def calc():
    res = int(val1.get()) + int(val2.get())
    valSum.set(res)

validate = root.register(validateInput)

Entry(root, width=9, textvariable=val1, validate="key", validatecommand=(validate, "%P")).grid(row=0, column=0)
Label(root, text="+").grid(row=0, column=1)
Entry(root, width=9, textvariable=val2, validate="key", validatecommand=(validate, "%P")).grid(row=0, column=2)
Label = Label(root, text="=").grid(row=0, column=3)
Entry(root, width=9, textvariable=valSum, state="readonly").grid(row=0, column=4)
Button(root, text="求和", command=calc).grid(row=1, column=0, columnspan=5, sticky=EW)

root.mainloop()
