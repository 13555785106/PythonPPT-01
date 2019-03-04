#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
python mymodule.py -v
"""


def square(x):
    '''
    square(x)

    返回 x 的平方
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x * x


def str_plus(str1, str2):
    '''
    连接两个字符串，返回一个新的字符串

    >>> str_plus("hello", " python")  # doctest: +ELLIPSIS
    'hello ...'

    '''
    return str1 + str2


def group_by_length(words):
    """Returns a dictionary grouping words into sets by length.

    >>> grouped = group_by_length([ 'python', 'module', 'of', 'the', 'week' ])
    >>> grouped == { 2:set(['of']),
    ...              3:set(['the']),
    ...              4:set(['week']),
    ...              6:set(['python', 'module']),
    ...              }
    True

    """
    d = {}
    for word in words:
        s = d.setdefault(len(word), set())
        s.add(word)
    return d


if __name__ == '__main__':
    import doctest, mymodule

    doctest.testmod(mymodule)

# send(msg)方法的参数msg指定的是
# 上一次被挂起的yield语句的返回值。
def seq2(start):
    while True:
        ret = yield start
        #print ret
        if ret:
            start = ret
        start += 1


def seq1(start):
    while True:
        yield start
        start += 1
