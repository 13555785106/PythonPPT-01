#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter

root = Tkinter.Tk()
# 创建一个Label，其父部件是 root
label = Tkinter.Label(root, \
                      font=("Times", "64", "bold italic"), \
                      text='你好,世界!')
label.pack()
Tkinter.mainloop()  # 进入消息循环
