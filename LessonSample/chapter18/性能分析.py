#!/usr/bin/python
# -*- coding: UTF-8 -*-

import profile


def func01():
    for x in xrange(100000000):
        pass


profile.run('mymodule.square(9)')
profile.run('func01()')
# profile.run('mymodule.square(9)',u'性能分析结果.txt')
# ret = pstats.Stats(u'性能分析结果.txt')
# print dir(ret)
# print ret.stats
'''其中输出每列的具体解释如下：

●ncalls：表示函数调用的次数；
●tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
●percall：（第一个 percall）等于 tottime/ncalls；
●cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
●percall：（第二个 percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
●filename:lineno(function)：每个函数调用的具体信息；
'''
