#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

root = tk.Tk()
v = tk.IntVar()
tk.Label(root,
         text="""请选一门程序设计语言:""",
         justify=tk.LEFT,
         padx=20).pack()
tk.Radiobutton(root,
               text="Python",
               padx=20,
               variable=v,
               value=1).pack(anchor=tk.W)
tk.Radiobutton(root,
               text="Perl",
               padx=20,
               variable=v,
               value=2).pack(anchor=tk.W)
root.mainloop()
