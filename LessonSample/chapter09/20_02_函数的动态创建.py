#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 动态创建函数

from types import *

funstr = """

sex = "男"

def func01():
    return "func01"
    
def func02():
    return "func02"
"""

module_code = compile(funstr, '', 'exec')
exec module_code
print module_code.co_names
funcs = {}
for v in module_code.co_consts:
    if isinstance(v, CodeType):
        funcs[v.co_name] = FunctionType(v, {})
    print type(v), dir(v)

print func01(), func02()
print funcs['func01'](), funcs['func02']()
