#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def callback(event):
    # print("获取的键盘值：",event.keysym)  #可以获取所有的键盘值，但是对于输入法输入的中文等不能识别，为??
    # print("获取的输入值：",event.char) #获取用户输入，对于特殊，像shift等是不能捕获，为空

    char = event.char
    if not char:
        char = event.keysym

    print "获取的值：", char

frame = Frame(root, width=200, height=200)
frame.pack()
# 绑定事件
frame.bind("<KeyRelease>", callback)  # 键盘按键Key, KeyPress, KeyRelease
frame.focus_set()

root.mainloop()
