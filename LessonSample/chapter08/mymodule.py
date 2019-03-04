#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ---------全局代码---------加载就被执行
var01 = 1
var02 = 'Tom'
print var01, var02
print __name__
if __name__ == '__main__':
    # 可以通过 __name__ 属性来判断文件是以主程序运行
    # 还是以模块加载，来决定运行那些代码
    print __file__, '以主程序运行'
else:
    print __file__, '以模块加载'

# ---------全局代码---------
def func01():
    print 'func01被执行！'
