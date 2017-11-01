#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承和多态
'''
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000
'''
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
        
    def eat(self):
        print('Eating fish...')    

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
cat.eat()

