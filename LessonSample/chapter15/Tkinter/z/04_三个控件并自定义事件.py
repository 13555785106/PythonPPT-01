#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

root = Tk()
root.geometry('320x240')
# 创建一个Label，其父部件是 top
hellolabel = Label(root, \
                   font="Times 40 bold italic", \
                   text='Hello World!')
hellolabel.pack(fill=BOTH, expand=1)

def resize(val):
    print "Times %s bold italic" % (val)
    hellolabel.config(font="Times %s bold italic" % (val))
    pass

fontscale = Scale(root, from_=10, to=40, orient=HORIZONTAL, command=resize)
fontscale.set(20)
fontscale.pack(fill=BOTH, expand=1)

quitbutton = Button(root, \
                    font="Times 24 bold italic", \
                    text='QUIT', \
                    activeforeground='white', \
                    activebackground='red', \
                    command=root.quit)
quitbutton.pack()
mainloop()  # 进入消息循环
