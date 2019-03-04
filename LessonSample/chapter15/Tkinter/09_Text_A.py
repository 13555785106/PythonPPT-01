#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()
text.insert(INSERT, "66666")
text.insert(END, "888888")
text.insert(CURRENT, "77777")
text.insert(INSERT, "99999")
root.mainloop()

# Special tags, marks and insert positions
# SEL='sel'         #选择的文字被替换
# SEL_FIRST='sel.first' #选中的文字的前面插入
# SEL_LAST='sel.last'   #选中的文字后面被插入
# END='end'         #在当前文档结尾插入
# INSERT='insert'   #在当前光标位置插入
# CURRENT='current' #在当前位置插入
# ANCHOR='anchor'
# ALL='all' # e.g. Canvas.delete(ALL)


# def insert(self, index, chars, *args):
#     """Insert CHARS before the characters at INDEX. An additional
#     tag can be given in ARGS. Additional CHARS and tags can follow in ARGS."""
#     self.tk.call((self._w, 'insert', index, chars) + args)


