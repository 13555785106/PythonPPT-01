#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
text = Text(root, height=4, width=50, relief=SUNKEN)
scrollbar.pack(side=RIGHT, fill=Y, expand=1)
text.pack(side=LEFT, fill=BOTH, expand=1)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# text.grid(row=0, column=0, sticky="nsew")

# scrollbar.grid(row=0, column=1, sticky="ns")

scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""

text.insert(END, quote)
root.mainloop()
