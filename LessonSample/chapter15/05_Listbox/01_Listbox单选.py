#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

listbox = Listbox(root)

listbox.pack()

for item in ["Java", "C#", "Objective-C", 'Python', 'JavaScript', 'CSS', 'HTML', 'SQL']:
    listbox.insert(END, item)  # 插入方向，从后方...（是按照索引来的）

buttonDelete = Button(root, text="删除当前选中", command=lambda x=listbox: x.delete(ACTIVE))
buttonDelete.pack()
root.mainloop()
