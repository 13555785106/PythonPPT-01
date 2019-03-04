#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

def printInfo():
    print("Tkinter是非常容易使用的!")

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
                   command=quit)
button.pack(side=tk.LEFT)
# 这个Button的command指定了上面定义的函数
slogan = tk.Button(frame,
                   text="你好",
                   command=printInfo)
slogan.pack(side=tk.LEFT)

root.mainloop()
