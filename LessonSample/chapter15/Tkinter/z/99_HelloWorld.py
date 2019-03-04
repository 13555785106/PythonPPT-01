#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "你好朋友们!"

    def createWidgets(self):
        self.QUIT = Button(self, font=("宋体", "32", "bold"))
        self.QUIT["text"] = "退出"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self, font=("宋体", "32", "bold"))
        self.hi_there["text"] = "你好",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
# root.destroy()
