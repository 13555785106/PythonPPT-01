#!/usr/bin/python
# -*- coding: UTF-8 -*-
emps = []
fo = open('employees.txt', 'r')
index = 0
while True:
    line = fo.readline()
    if index > 0:
        if len(line) > 0:
            emps.append(line.strip().split(","))
        else:
            break
    index += 1
fo.close()
print emps


def empName(emp):
    return emp[1] + ' ' + emp[2]


def empCommissionPct(emp):
    if len(emp[8]) == 0:
        return '0'
    else:
        return emp[8]


def cmpEmp(emp1, emp2):
    return cmp(emp1[1] + ' ' + emp1[2], emp2[1] + ' ' + emp2[2])


# emps.sort(cmp=cmpEmp)
emps.sort(key=empCommissionPct, reverse=False)

fo = open("employees01.txt", "w")
print '------------------------------------'
for emp in emps:
    print "commissionPct", "=", emp[8]
for emp in emps:
    num = len(emp)
    # for index in range(num):
    #    fo.write(emp[index])
    #    if index < num - 1: fo.write(',')
    for index, attr in enumerate(emp):
        fo.write(attr)
        if index < num - 1: fo.write(',')
    fo.write('\r\n')
print '------------------------------------'
fo.close()
