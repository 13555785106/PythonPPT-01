#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

import mymodule


class MyModuleTestCase(unittest.TestCase):
    def testSquare(self):
        for x in xrange(10):
            ret = mymodule.square(x)
            self.failUnless(ret == x * x, '%d 求平方失败' % x)

    def testStrPlus(self):
        for x in xrange(5):
            for y in xrange(5):
                ret = mymodule.str_plus(str(x), str(y))
                self.assertEquals(ret, str(x) + ' ' + str(y), '%s 与 %s 拼接失败' % (str(x), str(y)))


if __name__ == '__main__':
    # unittest.main():使用她可以方便的将一个单元测试模块变为可直接运行的测试脚本，
    # main()方法使用TestLoader类来搜索所有包含在该模块中以“test”命名开头的测试方法，并自动执行他们。
    # 执行方法的默认顺序是：根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。
    # 所以以A开头的测试用例方法会优先执行，以a开头会后执行。
    unittest.main()
