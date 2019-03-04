#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter

root = Tkinter.Tk()
# 创建一个Label，其父部件是 top
hellolabel = Tkinter.Label(root, \
                            font=("Times", "64", "bold italic"), \
                            text='Hello World!')
hellolabel.pack()

quitbutton = Tkinter.Button(root, \
                            font=("Times", "32", "bold italic"), \
                            bg='red',\
                            text='QUIT',\
                            command=root.quit)
quitbutton.pack(fill=Tkinter.X,expand=1)
Tkinter.mainloop()  # 进入消息循环
