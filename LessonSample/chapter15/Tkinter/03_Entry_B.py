#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

labelTitle = Label(root, text="书名:").grid(row=0, column=0)
labelAuthor = Label(root, text="作者:").grid(row=1, column=0)

entryTitle = Entry(root)
entryTitle.grid(row=0, column=1, padx=10, pady=5)
entryAuthor = Entry(root)
entryAuthor.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("作品：%s" % entryTitle.get())
    print("作者：%s" % entryAuthor.get())

Button(root, text="打印数据", command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

root.mainloop()
