#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter

class MyApp:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title("App")
        self.root.geometry("400x400")
        self.root.update()
        self.box1Text = Tkinter.Text(self.root, width=1, height=1)
        self.box1Text.pack(fill=Tkinter.BOTH,side=Tkinter.LEFT, expand=True)
        self.box2Text = Tkinter.Text(self.root, width=1, height=1)
        self.box2Text.pack(fill=Tkinter.BOTH,side=Tkinter.RIGHT, expand=True)

App = MyApp()
App.root.mainloop()