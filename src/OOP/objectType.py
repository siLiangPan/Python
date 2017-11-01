#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 使用type()
print(type(123))
print(type('str'))
print(type(None))

print(type(abs))

type(123)==int
type('abc')==str


import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也可以用isinstance()判断：
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)
# isinstance(d, Dog) and isinstance(d, Animal)



# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：


