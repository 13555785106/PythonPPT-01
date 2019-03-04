#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
from tkMessageBox import *

root = Tk()

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        root.quit()
    else:
        showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
root.mainloop()
