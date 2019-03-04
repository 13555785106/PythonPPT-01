#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv

with open('emps01.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, dialect=csv.excel)
    csvwriter.writerow(["NAME", "AGE", "SALARY"])
    csvwriter.writerow(['Tom', 36, 9888.67])
    csvwriter.writerow(['John', 24, 4000.50])

with open('emps02.csv', 'wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=["NAME", "AGE", "SALARY"], dialect=csv.excel)
    csvwriter.writeheader()
    csvwriter.writerow({"NAME": 'Tom', "AGE": 36, "SALARY": 9888.67})
    csvwriter.writerow({"NAME": 'John', "AGE": 24, "SALARY": 4000.50})
