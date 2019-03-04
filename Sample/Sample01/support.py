# -*- coding: UTF-8 -*-
def print_func(par):
    global g
    a,b,c=1,2,3
    print '全局变量'
    globalVars = globals()
    for k in globalVars:
        print k,'=',globalVars[k]
    print '局部变量'
    localVars = locals()
    for k in localVars:
        print k,'=',localVars[k]
    print "Hello : ", par
    return
