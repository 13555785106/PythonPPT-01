#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

root = tk.Tk()
intVar = tk.IntVar()
intVar.set(1)  # 值为1，默认选中第二项
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print(intVar.get())

tk.Label(root,
         text="""请你选一门你喜欢的程序设计语言:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, language in enumerate(languages):
    print val, language
    tk.Radiobutton(root,
                   indicatoron=1,
                   text=language,
                   padx=20,
                   variable=intVar,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
