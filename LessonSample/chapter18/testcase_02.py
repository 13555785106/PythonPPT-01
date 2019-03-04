#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def tearDown(self):
        print('tearDown')

    def setUp(self):
        print('setUp')

    def test_run4(self):
        print 'test_run4'
        # self.assertEqual(1,1)
        self.assertIs(1, 1)

    def test_run2(self):
        print 'test_run2'
        # self.assertEqual(1,1)
        self.assertIs(1, 1)

    def test_run3(self):
        print 'test_run3'
        # self.assertEqual(1,1)
        self.assertIs(1, 1)

    def test_run1(self):
        print 'test_run1'
        # self.assertEqual(1,1)
        self.assertIs(1, 1)


if __name__ == '__main__':
    # 创建一个测试集合
    test_suite = unittest.TestSuite()
    # 测试套件中添加测试用例
    # test_suite.addTest(MyTest('test_run1'))
    # 使用makeSuite方法添加所有的测试方法
    test_suite.addTest(unittest.makeSuite(MyTest))
    # 生成执行用例的对象
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
    # 执行测试套件
