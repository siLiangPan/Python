#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义类是通过class关键字
class Student(object):
    # 对象属性
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 对象的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
        
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
print(bart.get_grade())
lisa.print_score()
print(lisa.get_grade())