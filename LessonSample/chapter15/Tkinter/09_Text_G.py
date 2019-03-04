#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

root = Tk()
text = Text(root, width=32, height=6, font=("Times", "16", "bold italic"))
text.pack()
paragraph = '''012345678901234567890123456789
012345678901234567890123456789
012345678901234567890123456789'''
text.insert(CURRENT, paragraph)
contents = text.get(1.0, END)

def getData(contents):
    data = hashlib.md5(contents.encode())
    return data.hexdigest()

cont = getData(contents)

def check():
    data = getData(text.get(1.4, END))
    if data != cont:
        print("内容不一致")
    else:
        print("检测通过")

Button(root, text="检测", command=check).pack()
root.mainloop()
