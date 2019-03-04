#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
text = Text(root, width=48, height=24)
text.pack()
text.insert(INSERT, "AAAAA")
text.insert(END, "ZZZZZ")
# 注意photo对象写在函数体外，若在函数体中，生存周期一到，就会被释放。
photoImage = PhotoImage(file="python.gif")

# 此时是事件button点击，进入处理，处理后，才会进入IO循环中去显示数据，
# 若是数据在函数体中被回收，那么久无法显示出来。
# 字符串是被存放在常量区，不会被删除的，所以两个的id是一致的。
def insertSomething():
    text.image_create(INSERT, image=photoImage)
    text.insert(END, '神一样的存在')

button = Button(text, text="点击会插入内容", command=insertSomething)
# 要想显示控件，需要将text设置为窗口（"""Create a window at INDEX."""）
text.window_create(INSERT, window=button)

root.mainloop()
