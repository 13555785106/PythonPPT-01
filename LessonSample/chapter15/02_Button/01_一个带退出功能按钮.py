#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter

root = Tkinter.Tk()
# 创建一个Label，其父部件是 top
quitbutton = Tkinter.Button(root, \
                            font=("Times", "32", "bold italic"), \
                            text='退出', command=root.quit)
quitbutton.pack()
Tkinter.mainloop()  # 进入消息循环
