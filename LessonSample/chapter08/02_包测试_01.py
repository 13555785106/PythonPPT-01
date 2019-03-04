#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入包，会直接导入 __init__.py文件，其它模块不会被加载
# 子包及子模块不会被加载!
import mypackage

# mypackage.mymodule01.printinfo() 此时运行这段代码会出错

import mypackage.mymodule01

mypackage.mymodule01.printinfo()

import mypackage.mymodule02

mypackage.mymodule02.printinfo()
