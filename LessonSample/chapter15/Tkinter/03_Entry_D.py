#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
varAccountErrorMsg = StringVar()
varAccountErrorMsg.set('')
varPasswordErrorMsg = StringVar()
varPasswordErrorMsg.set('')
Label(root, textvariable=varAccountErrorMsg, fg='red').grid(row=0, column=2)
Label(root, textvariable=varPasswordErrorMsg, fg='red').grid(row=1, column=2)
Label(root, text="账号:").grid(row=0, column=0)
Label(root, text="密码:").grid(row=1, column=0)

def validateAccount():
    if entryAccount.get() == "root":
        varAccountErrorMsg.set('')
        return True
    else:
        entryAccount.delete(0, END)
        varAccountErrorMsg.set('账号错误，必须是 root')
        return False

def validatePassword():
    if entryPassword.get() == "123456":
        varPasswordErrorMsg.set('')
        return True
    else:
        entryPassword.delete(0, END)
        varPasswordErrorMsg.set('密码错误，必须是 123456')
        return False

entryAccount = Entry(root, validate="focusout", validatecommand=validateAccount)
entryAccount.grid(row=0, column=1, padx=10, pady=5)
entryPassword = Entry(root, show="*", validate="focusout", validatecommand=validatePassword)
entryPassword.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
