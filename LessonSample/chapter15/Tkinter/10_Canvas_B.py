#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100, fill="green", width=3)  # width是线宽
w.create_line(200, 0, 0, 100, fill="green", width=3)
w.create_rectangle(40, 20, 160, 80, fill="blue")
w.create_rectangle(65, 35, 135, 65, fill="#FF9966")

# 填充文字
w.create_text(100, 50, text="你好")

root.mainloop()
