#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

print isinstance(cat, Cat)
print isinstance(cat, Animal)

run_twice(dog)
run_twice(cat)

print type(cat) == Animal
print dir(dog)