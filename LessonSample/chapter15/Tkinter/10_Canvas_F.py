#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
charSign = {1: 'error', 2: 'info', 3: 'question', 4: 'hourglass'}
for i in charSign:
    cv.create_bitmap((20 * i, 20 * i), bitmap=charSign[i])
cv.pack()
root.mainloop()
# 使用bitmap属性来指定位图的名称，这个函数的第一个参数为一个点(x,y)指定位图存放位置的左上位置。
