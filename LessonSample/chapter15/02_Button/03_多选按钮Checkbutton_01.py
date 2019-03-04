#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
fruits = ["苹果", '香蕉', '桃子', '橙子', '猕猴桃']
dictMap = {}
for fruit in fruits:
    dictMap[fruit] = BooleanVar()

def change():
    line = ''
    for index in xrange(len(fruits)):
        line += fruits[index] + ':' + str(dictMap[fruits[index]].get())
        if index < len(fruits) - 1:
            line += ","
    print line

for fruit in fruits:
    # 使用一个固有变量来记录状态
    b = Checkbutton(root, text=fruit, variable=dictMap[fruit], command=change)
    b.pack(anchor=W)  # 控件相对主窗口在左边
root.mainloop()
