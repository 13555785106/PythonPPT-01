#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

listbox = Listbox(root, fg='#FF9966', bg='#339933', font=("Times", "16", "bold italic"), selectmode=EXTENDED)

listbox.pack(padx=4)

for item in ('Java', 'C', 'C++', 'Python', 'C#', 'PHP', 'JavaScript', 'SQL', 'SWIFT', 'Perl'):
    listbox.insert(END, ' ' + item)  # 插入方向，从后方...（是按照索引来的）

def deleteSelectedItems():
    selectedItems = list(listbox.curselection())
    selectedItems.reverse()  # 需要先翻转过来，在从后向前删除（不然删除会导致索引不及时，删错元素）

    for index in selectedItems:
        listbox.delete(index)

Button(root, text="删除,可多选", command=deleteSelectedItems).pack()
root.mainloop()
