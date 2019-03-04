#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import hashlib

root = Tk()
text = Text(root, width=30, height=5)
text.pack()
paragraph = '''0123456789abc01234567890123456789
01234567890123456789abc0123456789
012345678901234567890123456789'''
text.insert(CURRENT, paragraph)
start = '1.0'
while True:
    pos = text.search('abc', start, stopindex=END)
    if not pos:
        break
    print pos
    start = pos + "+1c"

mainloop()
