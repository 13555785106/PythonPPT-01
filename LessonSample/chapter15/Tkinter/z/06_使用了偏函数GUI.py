#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'
SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}
critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

root = Tk()
root.title('Road Signs')
Button(root, text='QUIT', command=root.quit, bg='red', fg='white').pack()

MyButton = pto(Button, root)

CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')
for eachSign in SIGNS:
    print eachSign
    signType = SIGNS[eachSign]
    print signType
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
        signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
    print cmd
    eval(cmd)
root.mainloop()
