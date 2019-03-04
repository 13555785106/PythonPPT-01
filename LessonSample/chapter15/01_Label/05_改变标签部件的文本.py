#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

counter = 0

def counter_label(label):
    def count():
        global counter
        counter += 1
        # 通过config函数修改文本
        label.config(text=str(counter))
        # after函数第一个参数是时间，单位毫秒。
        # 第二个参数经过这个时间之后要执行的函数。
        label.after(1000, count)

    count()

root = tk.Tk()
root.title("读秒器")
label = tk.Label(root, fg="#FF9966", font="Helvetica 64 bold")
label.pack()
counter_label(label)
button = tk.Button(root, text='STOP', width=12, font="Arial 24 bold", command=root.destroy)
button.pack()
root.update()
width = root.winfo_reqwidth()
height = root.winfo_reqheight()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (
    width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)

# 设置窗口是否可变长、宽，True：可变，False：不可变
root.resizable(width=True, height=True)

root.mainloop()
