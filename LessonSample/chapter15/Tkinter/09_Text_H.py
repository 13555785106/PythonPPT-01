#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "fea g ag awgwag\r\n")
text.insert(INSERT, "ffge g agge awgag")

def getIndex(text, index):  # 因为这个索引是一个小数 n.m    n行m列，所以我们需要进一步处理
    print(text, index)
    return tuple(map(int, str.split(text.index(index), '.')))
    # map(func,iter) 这里func-->int()  iter--->[n,m]可迭代

start = '1.0'

while True:
    pos = text.search('g', start, stopindex=END)
    if not pos:
        break
    print getIndex(text, pos)
    start = pos + "+1c"

mainloop()
