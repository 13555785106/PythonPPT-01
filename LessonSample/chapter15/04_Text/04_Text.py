#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=36, height=8, font=("Times", "18", "bold italic"))
text.pack()
paragraph = '''012345678901234567890123456789
012345678901234567890123456789
012345678901234567890123456789'''
text.insert(CURRENT, paragraph)

text.tag_add("tag1", "1.7", "1.12", "1.16")
text.tag_config("tag1", background="green", foreground="red")
text.tag_add("tag2", "1.9","1.12","2.9", "2.12", "3.15", "3.18")
text.tag_config("tag2", background="blue", foreground="white",font=("Times", "32"))


# text.tag_lower("tag2")  # 降低
# text.tag_raise("tag1")  #提高

root.mainloop()
