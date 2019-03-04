#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

    def count2(self):
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
# 在类的对象生成后,调用含有类私有属性的函数时就可以使用到私有属性.
counter.count()
# 第二次同样可以.
print 'publicCount=',counter.publicCount
print '__secretCount',counter._JustCounter__secretCount  # 不改写报错，实例不能访问私有变量
try:
    counter.count2()
except IOError:
    print "不能调用非公有属性!"
else:
    print "ok!"  # 现在呢!证明是滴!
