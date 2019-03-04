#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()
text.insert(INSERT, "01234567890123456789\n")
text.insert(END, "01234567890123456789\n")
text.insert(INSERT, "01234567890123456789")
text.insert('2.2', '插入的文字')

print text.get('1.5','1.9')
print text.get('2.5','3.9')
root.mainloop()
