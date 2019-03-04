#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

Label(root, text="账号:").grid(row=0, column=0)
Label(root, text="密码:").grid(row=1, column=0)

varAccount = StringVar()
varPassword = StringVar()

entryAccount = Entry(root)
entryAccount.grid(row=0, column=1, padx=10, pady=5)
entryPassword = Entry(root, show="*")
entryPassword.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("账号：%s" % entryAccount.get())
    print("密码：%s" % entryPassword.get())

Button(root, text="打印数据", command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

root.mainloop()
