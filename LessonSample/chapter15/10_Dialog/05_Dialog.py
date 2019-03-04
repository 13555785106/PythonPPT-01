#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
import Dialog

root = Tk()
DIALOG_ICON = 'warning'

def confirm():
    d = Dialog.Dialog(root, {'title': '文件已修改',
                             'text':
                                 '文件"Python.h"已经被修改，'
                                 '退出前你想保存吗？',
                             'bitmap': DIALOG_ICON,
                             'default': 0,
                             'strings': ('保存文件',
                                         '忽略',
                                         '返回编辑器')})
    print d.num

Button(root, {'text': '测试',
              'command': confirm,
              Pack: {'fill': X, 'expand': 1}})
Button(root, {'text': '退出',
              'command': root.quit,
              Pack: {}})
root.mainloop()
