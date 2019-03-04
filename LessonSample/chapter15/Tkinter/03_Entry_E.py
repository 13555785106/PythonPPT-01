#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
Label(root, text="账号:").grid(row=0, column=0)
Label(root, text="密码:").grid(row=1, column=0)

def validateAccount(v1, v2, v3, v4, v5, v6):
    print(v1, v2, v3, v4, v5, v6)
    if v1 == 'root':
        return True
    else:
        return False

strAccount = StringVar()

entryAccount = Entry(root, textvariable=strAccount, validate="focus",
                     validatecommand=(root.register(validateAccount),
                                      "%P", "%s", "%v", "%V", "%i", "%d"))

entryAccount.grid(row=0, column=1, padx=10, pady=5)
entryPassword = Entry(root)
entryPassword.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
