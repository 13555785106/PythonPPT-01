#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def callback():
    print("---Hello World---")

menubar = Menu(root)

menubar.add_command(label="文件", command=callback)
menubar.add_command(label="退出", command=root.quit)

frame = Frame(root, width=300, height=240)
frame.pack()

def popup(event):
    print event.x, event.y
    print event.x_root, event.y_root
    menubar.post(event.x_root, event.y_root)
    # post是相对于整个屏幕，而不是程序窗口，
    # 而event.x/y是获取的相对于程序窗口的尺寸，
    # 所以我们需要使用event.x_root/y_root去获取屏幕尺寸

# frame是一个框架区域，其中可以包含其他控件，是一个独立的区域划分，我们在这个区域中绑定事件
frame.bind("<Button-3>", popup)  # -1是左键，-2是中间滑轮点击，-3是右键
root.config(menu=menubar)

root.mainloop()
