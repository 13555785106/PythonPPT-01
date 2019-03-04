#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

root = tk.Tk()
tk.Label(root,
         text="\"Times Font\"字体的红色文本",
         fg="red",
         font="Times").pack()
tk.Label(root,
         text="\"Helvetica Font\"字体的绿色粗体文本",
         fg="light green",
         bg="dark green",
         font="Helvetica 24 bold italic").pack()
tk.Label(root,
         text="\"Verdana\"的蓝色倾斜文本",
         fg="blue",
         bg="yellow",
         font="Verdana 18 bold").pack()
root.mainloop()
