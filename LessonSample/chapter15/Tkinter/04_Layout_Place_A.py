#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

photoImage = PhotoImage(file="lion.gif")
Label(root, image=photoImage).pack()  # 会被button覆盖

def click():
    print("我才是中心!")

Button(root, text="无论窗口如何变化\n我都是中心", command=click) \
    .place(relx=0.5, rely=0.5, anchor=CENTER)  # relx和rely是设置在窗口的位置在中间，anchor是设置这个控件相对于窗口中间的位置

root.mainloop()
