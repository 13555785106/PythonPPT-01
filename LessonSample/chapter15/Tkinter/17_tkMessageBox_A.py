#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox;

root = Tk()

print tkMessageBox.askokcancel("title", "question")

root.mainloop()
