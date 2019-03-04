#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk

master = tk.Tk()
explanation = """   据共同社11月7日报道，在共和党在中期选举中失去了众议院控制权的次日，特朗普在一次记者招待会上讲话表示，虽然他称日本首相安倍晋三为“与我关系最亲近的人士之一”，但他说，“我一直跟他说日本在贸易上并没有公平对待美国”。
    特朗普说：“他们以非常低的关税将数百万辆汽车输入美国，却不买我们的汽车。”
    特朗普批评了日本对美国的贸易顺差，并补充说，“但是别觉得孤单，因为你们并非独一无二”。"""
msg = tk.Message(master, text=explanation)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
tk.mainloop()
