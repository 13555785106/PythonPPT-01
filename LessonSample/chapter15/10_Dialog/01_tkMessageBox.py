#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
import tkMessageBox

root = Tk()

def answer():
    tkMessageBox.showerror("Answer", "Sorry, no answer available")

def callback():
    if tkMessageBox.askyesno('Verify', 'Really quit?'):
        root.quit()
    else:
        tkMessageBox.showinfo('No', 'Quit has been cancelled')

Button(root, text='Quit', command=callback).pack(fill=X)
Button(root, text='Answer', command=answer).pack(fill=X)
root.mainloop()
