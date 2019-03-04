#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=48, height=24)
text.pack()

text.insert(CURRENT,
            "012345678901234567890123456789\n012345678901234567890123456789\n012345678901234567890123456789\n012345678901234567890123456789\n012345678901234567890123456789\n")

"""
# 插入时标记会后移
text.mark_set("bj", "1.5")
text.insert("bj", "美国")
text.insert("bj", '中国')
text.mark_unset("bj")
"""

"""
# 删除时标记会前移
text.mark_set("bj", "1.5")
text.delete(1.4, 1.7)
text.insert("bj", "美国")
text.insert("bj", '中国')
text.mark_unset("bj")
"""

# 以上都是插入在右侧，下面插入在左侧

text.mark_set("bj", "1.5")
text.mark_gravity("bj", LEFT)
text.insert("bj", "美国")
text.insert("bj", '中国')
text.mark_unset("bj")

root.mainloop()
