#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
from math import *

def evaluate(event):
    res.configure(text="结果: " + str(eval(entry.get())))

root = Tk()
Label(root, text="请输入表达式:").pack()
entry = Entry(root)
#绑定回车事件
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(root)
res.pack()
root.mainloop()
