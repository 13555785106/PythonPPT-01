#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ftplib, random

ftp = ftplib.FTP()
# 连接FTP服务器
ftp.connect('ftp.ncdc.noaa.gov', 21)
# 匿名登录
ftp.login('anonymous', '')
filelist = []
# 列出当前目录
ftp.dir('.', filelist.append)
# 提取文件列表
files = [f.split(None, 8)[-1] for f in filelist if f.startswith('-')]
print files
# 提取目录列表
dirs = [f.split(None, 8)[-1] for f in filelist if f.startswith('d')]
print dirs
# 随机选择一个文件
f = random.choice(files)
buf_size = 1024
fp = open(f, 'wb')
# 下载这个文件
ftp.retrbinary('RETR ' + f, fp.write, buf_size)
ftp.set_debuglevel(0)
fp.close()
print f
ftp.close()
