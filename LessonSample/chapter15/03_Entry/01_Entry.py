#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

def showPersonalInfo():
    print "名: %s，姓: %s".decode('utf-8') % (entryFirstName.get(), entryLastName.get())

root = Tk()
Label(root, text="名:").grid(row=0)
Label(root, text="姓:").grid(row=1)

entryFirstName = Entry(root)
entryLastName = Entry(root)

entryFirstName.grid(row=0, column=1)
entryLastName.grid(row=1, column=1)

Button(root, text='退出', command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(root, text='显示', command=showPersonalInfo).grid(row=3, column=1, sticky=E, pady=4)

root.mainloop()
