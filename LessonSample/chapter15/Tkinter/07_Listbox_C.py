#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

# 1：生成滚动条
scrollBar = Scrollbar(root)
scrollBar.pack(side=RIGHT, fill=Y)

# 2：生成ListBox,将其与滚动条相关联,yscrollcommand
# （单向关联<Listbox去改变ScrollBar>：鼠标滚轮滚动内容，
# 滚动条会滑动，但是滚动条变化时，内容不会变化）
# 默认显示10条，我们可以设置滚轮或者height行数
listbox = Listbox(root, fg='#FF6699', font=("Times", "18", "bold"), selectmode=EXTENDED, height=10,
                  yscrollcommand=scrollBar.set)
listbox.pack()

# 3：将滚动条滚动事件与ListBox的视图显示相关联
# （单向关联<ScrollBar去改变Listbox>：滚动条变化时，内容会变化）
scrollBar.config(command=listbox.yview)

# 注意：2和3相关联会获得我们想要的结果

for item in range(100):
    listbox.insert(END, 'app-%09d' % item)  # 插入方向，从后方...（是按照索引来的）

root.mainloop()
