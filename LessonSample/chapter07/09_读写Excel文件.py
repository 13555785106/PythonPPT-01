#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd, xlwt, xlutils.copy

wb = xlutils.copy.copy(xlrd.open_workbook('emps.xls', formatting_info=True))
sheet = wb.get_sheet(0)
sheet.write(0, 0, u'肖俊峰')
wb.save('emps02.xls')
