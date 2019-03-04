#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

# PanedWindow和Frame相似，都是为组件提供一个框架，不过PanedWindow允许用户调整应用程序得空间划分

panedWindow = PanedWindow(root,orient=VERTICAL)
panedWindow.pack()
topLabel = Label(panedWindow, text="Top Paned")
panedWindow.add(topLabel)
bottomLabel = Label(panedWindow, text="Bottom Paned")
panedWindow.add(bottomLabel)
root.mainloop()
