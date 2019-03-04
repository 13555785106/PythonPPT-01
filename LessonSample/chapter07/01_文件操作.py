#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, shutil, time, sys, locale

# 获取当前工作目录
cwd = os.getcwd()
print cwd.decode(sys.getfilesystemencoding())
# 列出当前目录下的内容
for fn in os.listdir(cwd):
    print fn.decode(sys.getfilesystemencoding())  # 此处的编码与操作系统的默认编码相关

os.chdir(u'root')  # 进入 root
cwd = os.getcwd()
print cwd.decode(sys.getfilesystemencoding())
if not os.path.exists(cwd + '/a01'):
    os.mkdir('a01')
if not os.path.exists(cwd + '/a02/bb/cc/dd'):
    os.makedirs('a02/bb/cc/dd')
time.sleep(10)
os.rmdir('a01')
shutil.rmtree('a02')

'''    
print sys.getdefaultencoding()
print sys.getfilesystemencoding()
print locale.getdefaultlocale()
print sys.stdout.encoding
'''
