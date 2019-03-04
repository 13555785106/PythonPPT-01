#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
labelValue = IntVar()  # 选中为1，未选中为0
chackButton = Checkbutton(root, text="测试", variable=labelValue)
chackButton.pack()
label = Label(root, textvariable=labelValue)
label.pack()

root.mainloop()
