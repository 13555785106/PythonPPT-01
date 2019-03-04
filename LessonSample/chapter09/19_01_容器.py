#!/usr/bin/python
# -*- coding: UTF-8 -*-


class MyList(object):
    """简单容器的实现"""

    def __init__(self):
        self.array = ['a', 'b', 'c', 'd', 'e']

    def append(self, value):
        self.array.append(value)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __len__(self):
        return len(self.array)

    def __delitem__(self, index):
        del self.array[index]

list01 = MyList()
list01[2] = 'zzz'
print list01[0]
del list01[3]
print len(list01)
print '--------------------------'
for v in list01:
    print v
