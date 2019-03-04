#!/usr/bin/python
# -*- coding: UTF-8 -*-


class WebInfo:
    """
    双下划线的表示的是私有类型(private)的变量,
    只能是允许这个类本身进行访问了。
    """
    __site = "www.163.com"

    @classmethod
    def printsite(cls):
        print cls.__site;

    def __init__(self):
        pass
        self.__site = 'www.apache.org'  # 注释此行，看看结果

WebInfo.printsite()
# print WebInfo.__site #类私有变量确实不可直接访问
webinfo = WebInfo()
print webinfo._WebInfo__site  # 成员私有变量还是可以访问!!!
# print webinfo.__site
