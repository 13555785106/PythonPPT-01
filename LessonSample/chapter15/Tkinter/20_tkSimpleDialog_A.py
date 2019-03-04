#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkSimpleDialog

root = Tk()
root.update()

print tkSimpleDialog.askinteger("Spam", "鸡蛋数量:", initialvalue=12 * 12)
print tkSimpleDialog.askfloat("Spam", "大象重量\n(单位吨)", minvalue=1, maxvalue=100)
print tkSimpleDialog.askstring("Spam", "你的名字")

root.mainloop()
