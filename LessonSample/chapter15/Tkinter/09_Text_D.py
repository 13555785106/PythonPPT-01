#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

text = Text(root, width=48, height=24)
text.pack()

text.insert(CURRENT, "fgweagawgrhssdf")

# Marks标记

# 1.简单使用：
text.mark_set("bj", "1.3")  # 在1.3处设置标记，名为bj,就像书签一样，方便操作。注意mark_set和mark_unset对应
# 默认标记是记住右边的那个字符（第一次设置后就跟定他了）e字符
text.insert("bj", "66")  # fgw66eagawgrhssdf   向e字符左端插入
text.insert("bj", '88')  # fgw6688eagawgrhssdf 还是向e字符左端插入
text.mark_unset("bj")

text.delete(1.0, END)  # 清空数据

# 2.标志被删除了之后的反应：
text.insert(CURRENT, "fgweagawgrhssdf")
text.mark_set("bj", "1.3")  # 在1.3处设置标记，名为bj,就像书签一样，方便操作。注意mark_set和mark_unset对应
text.delete(1.2, 1.5)  # 注意当标记位置被删除了的话，会自动寻找到删除的字符串的下一个字符，以他为标志
# 删除字符串后面的那个紧接的字符是g，以他为标志
text.insert("bj", "66")  # fg66gawgrhssdf   向g字符左端插入
text.insert("bj", '88')  # fg6688gawgrhssdf 还是向g字符左端插入
text.mark_unset("bj")

text.delete(1.0, END)

# 3.前面都是以标志位为基准，放在右边。修改将标志位放在左边：mark_gravity
text.insert(CURRENT, "fgweagawgrhssdf")
text.mark_set("bj", "1.3")  # 在1.3处设置标记，名为bj,就像书签一样，方便操作。注意mark_set和mark_unset对应
text.mark_gravity("bj", LEFT)
# 默认标记是记住右边的那个字符（第一次设置后就跟定他了）e字符
text.insert("bj", "66")  # fgw66eagawgrhssdf   向e字符左端插入
text.insert("bj", '88')  # fgw6688eagawgrhssdf 还是向e字符左端插入
text.mark_unset("bj")

root.mainloop()
