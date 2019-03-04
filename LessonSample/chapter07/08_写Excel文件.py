#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt

wb = xlwt.Workbook(encoding='UTF-8')
sheet = wb.add_sheet('雇员表')
listdata = [
    ['汤姆', '男', 35],
    ['琼斯', '女', 28],
    ['Kaka', '男', 20]]
for rowNum in xrange(len(listdata)):
    for colNum in xrange(len(listdata[rowNum])):
        sheet.write(rowNum, colNum, listdata[rowNum][colNum])

wb.save('emps01.xls')

import xlrd, xlutils.copy
wb = xlutils.copy.copy(xlrd.open_workbook("emps.xls", formatting_info=True))
sheet = wb.get_sheet(0)
sheet.write(0, 0, u'肖俊峰')
wb.save('emps.xls')
