#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 动态创建类


def person_print_name(self):
    print(self.name)


def person_init(self, name):
    self.name = name


def person_str(self):
    return self.name


# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
Person = type("Person", (),
              {'__init__': person_init,
               '__str__': person_str,
               'print_name': person_print_name})
person = Person('肖俊峰')
print person
person.print_name()
print type(person)
print person.__class__
