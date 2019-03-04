#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv

with open('emps01.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, dialect=csv.excel)
    for row in csvreader:
        if csvreader.line_num > 1:
            print ', '.join(row)

with open('emps02.csv', 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile, dialect=csv.excel)
    for row in csvreader:
        print row["NAME"], row["AGE"], row["SALARY"]
