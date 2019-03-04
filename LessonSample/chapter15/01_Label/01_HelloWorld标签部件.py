#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

# 创建根部件
root = tk.Tk()
# 创建文字标签
labelHelloWorld = tk.Label(root, text="你好 Tkinter!")
# 进行布局
labelHelloWorld.pack()
# 进入主循环
root.mainloop()
