#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
text = Text(root, width=48, height=24)
text.pack()
text.insert(INSERT, "01234567890123456789\n")
text.insert(END, "01234567890123456789\n")

photoImage = PhotoImage(file="../python_icon_64.gif")

def insertSomething():
    text.image_create(INSERT, image=photoImage)
    text.insert(END, '神一样的存在')

button = Button(text, text="点击会插入内容", command=insertSomething)
# 要想显示控件，需要将text设置为窗口（"""Create a window at INDEX."""）
text.window_create(INSERT, window=button)

root.mainloop()
