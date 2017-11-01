#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass



class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
# 多重继承
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。        
class Dog(Mammal, Runnable):
    pass        

class Bat(Mammal, Flyable):
    pass