#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk
import tkMessageBox

def sayHello():
    tkMessageBox.showinfo('信息', '你好，程序员！')

def confirmQuit():
    if tkMessageBox.askyesno('提示', '确实要退出程序吗？'):
        quit()

root = tk.Tk()
# Frame主要用来布局的
frame = tk.Frame(root)
frame.pack()
# 创建了一个Button，点击会退出。
# command指定了点击执行的命令。
# QUIT是内置的命令。
button = tk.Button(frame,
                   text="退出",
                   fg="red",
                   font=("Times", "32", "bold italic"),
                   command=confirmQuit)
button.pack(side=tk.LEFT)
# 这个Button的command指定了上面定义的函数
slogan = tk.Button(frame,
                   text="你好",
                   font=("Times", "32", "bold italic"),
                   command=sayHello)
slogan.pack(side=tk.LEFT)

# 以下代码仅是将窗口居中
root.update()
width, height = root.winfo_reqwidth(), root.winfo_reqheight()
screenwidth, screenheight = root.winfo_screenwidth(), root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
# 设置窗口是否可变长、宽，True：可变，False：不可变
root.resizable(width=False, height=False)
root.mainloop()
