#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
print(os.name) # 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 注意uname()函数在Windows上不提供
#print(os.uname())

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))

'''
# 查看当前目录的绝对路径:
os.path.abspath('.')
#'/Users/michael'

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
#'/Users/michael/testdir'
# 拆分路径
os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# 得到文件扩展名
os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')

# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')



# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')
'''
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 列出当前目录下的所有目录
print(os.path.abspath('.'))
dirList = [x for x in os.listdir('E:\\workspace_psl\\IDE\\Python') if os.path.isdir(x)]
#dirList = [x for x in os.listdir('E:/workspace_psl/IDE/Python/src')]
print(dirList)

# 要列出所有的.py文件
fileList = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(fileList)
