#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
'''

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_name(self, name):
        self.__name = name
        
    def set_score(self, score):
        self.__score = score
        
        
bart = Student('Bart Simpson', 59)
# print(bart.__name)
# AttributeError: 'Student' object has no attribute '__name'
print(bart.get_name())
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
print(bart._Student__name)
