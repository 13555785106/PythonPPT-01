#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib


def progress(blocknum, blocksize, filelength):
    print blocknum, blocksize, filelength
    # print '%.2f%%' % ((blocknum * blocksize * 1.0) / filelength * 100)


# ret = urllib.urlretrieve("http://reg.email.163.com/unireg/call.do?cmd=register.entrance&from=163navi&regPage=163",'temp.html', progress)
ret = urllib.urlretrieve('http://mirrors.shu.edu.cn/centos/7.6.1810/isos/x86_64/CentOS-7-x86_64-Minimal-1810.iso',
                         'CentOS-7-x86_64-Minimal-1810.iso', progress)
print ret[1]
