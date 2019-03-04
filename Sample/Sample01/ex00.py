#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

for root, dirs, files in os.walk('.'):
    for name in files:
        print  root, name
    for name in dirs:
        print  root, name

'''
for fn in os.listdir(os.getcwd()):
    if fn.endswith(".gz"):
        file_name = cur_dir + os.sep + fn
        g_file = gzip.GzipFile(file_name)
        print g_file.readlines()
        g_file.close()
'''
