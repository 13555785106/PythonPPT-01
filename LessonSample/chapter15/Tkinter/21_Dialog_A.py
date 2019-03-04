#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
import Dialog

root = Tk()
DIALOG_ICON = 'warning'

def _test():
    d = Dialog.Dialog(None, {'title': 'File Modified',
                             'text':
                                 'File "Python.h" has been modified'
                                 ' since the last time it was saved.'
                                 ' Do you want to save it before'
                                 ' exiting the application.',
                             'bitmap': DIALOG_ICON,
                             'default': 0,
                             'strings': ('Save File',
                                         'Discard Changes',
                                         'Return to Editor')})
    print d.num

t = Button(root, {'text': 'Test',
                  'command': _test,
                  Pack: {}})
q = Button(root, {'text': 'Quit',
                  'command': t.quit,
                  Pack: {}})
root.mainloop()
