#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
    root = Tk()
    lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
    tgl = Checkbar(root, ['英国人', '德国人'])
    lng.pack(side=TOP, fill=X)
    tgl.pack(side=LEFT)
    lng.config(relief=GROOVE, bd=2)
    tgl.config(relief=GROOVE, bd=2)

    def allstates():
        print(list(lng.state()), list(tgl.state()))

    Button(root, text='退出', command=root.quit).pack(side=RIGHT)
    Button(root, text='查看', command=allstates).pack(side=RIGHT)
    root.mainloop()
