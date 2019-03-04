#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def mouseCallback(event):
    key = '左键'
    if event.num == 1:
        key = '左键'
    elif event.num == 2:
        key = '中键'
    elif event.num == 3:
        key = '右键'
    else:
        key = '未知'
    label.configure(text="%s:x=%d,y=%d" % (key, event.x, event.y))
    # label['text']= "%s:x=%d,y=%d" % (key, event.x, event.y)

def keyCallback(event):
    # print("获取的键盘值：",event.keysym)
    # print("获取的输入值：",event.char)
    # 获取用户输入，对于特殊，像shift等是不能捕获，为空

    char = event.char
    if not char:
        char = event.keysym
    label['text'] = char

label = Label(root, text='请随意按键盘或鼠标', width=18,
              height=3, bg='black',
              justify=CENTER, fg="#FF9966",
              font="Helvetica 24 bold italic")
label.pack(fill=BOTH, expand=1)
# 绑定事件
label.bind("<KeyRelease>", keyCallback)  # 键盘按键Key, KeyPress, KeyRelease
label.focus_set()
label.bind("<Button-1>", mouseCallback)  # 鼠标左键
label.bind("<Button-2>", mouseCallback)  # 鼠标滚轮
label.bind("<Button-3>", mouseCallback)  # 鼠标右键
root.mainloop()
