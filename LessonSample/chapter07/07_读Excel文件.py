#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd

wb = xlrd.open_workbook('emps.xls')
sheet = wb.sheets()[0]
print '行数', sheet.nrows
print '列数', sheet.ncols
print '------------------------------------------------------------------------'
for rowNum in xrange(sheet.nrows):
    print sheet.row_values(rowNum)
print '------------------------------------------------------------------------'
for colNum in xrange(sheet.ncols):
    print sheet.col_values(colNum)
print '------------------------------------------------------------------------'
for rowNum in xrange(sheet.nrows):
    line = u''
    for colNum in xrange(sheet.ncols):
        line += unicode(sheet.cell(rowNum, colNum).value)
        if colNum < sheet.ncols - 1:
            line += ','
    print line

print '------------------------------------------------------------------------'
for rowNum in xrange(sheet.nrows):
    print ",".join([unicode(x) for x in sheet.row_values(rowNum)])
wb.release_resources()
