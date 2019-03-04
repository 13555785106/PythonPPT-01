#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

def callback():
    var.set("你好世界！")

root = Tk()

var = StringVar()
var.set("Hello World!")

frame1 = Frame(root, bg='blue')
frame2 = Frame(root, bg='green')

lebelText = Label(frame1, textvariable=var, padx=20)
lebelText.pack(side=LEFT)

img = PhotoImage(file="lion.gif")
labelImage = Label(frame1, image=img)
labelImage.pack(side=RIGHT)

btnCm = Button(frame2, text="下一步", command=callback)
btnCm.pack()

frame1.pack(fill=BOTH, expand=1, padx=2, pady=2)
frame2.pack(fill=BOTH, expand=1, padx=2, pady=2)

root.mainloop()
