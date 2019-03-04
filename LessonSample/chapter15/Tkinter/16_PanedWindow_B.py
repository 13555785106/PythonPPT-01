#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

# PanedWindow和Frame相似，都是未组件提供一个框架，不过PanedWindow允许用户调整应用程序得空间划分

panedWindow1 = PanedWindow(root, showhandle=True, sashrelief=SUNKEN)  # 默认水平  showhandle显示手柄，sashrelief显示边框
panedWindow1.pack(fill=BOTH, expand=1)

leftLabel = Label(panedWindow1, text="左")
panedWindow1.add(leftLabel)

panedWindow2 = PanedWindow(root, orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)

panedWindow1.add(panedWindow2)

topLabel = Label(panedWindow2, text="上")
bottomLabel = Label(panedWindow2, text="下")
panedWindow2.add(topLabel)
panedWindow2.add(bottomLabel)

root.mainloop()
