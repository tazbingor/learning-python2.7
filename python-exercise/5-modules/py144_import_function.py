#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午8:40
# @Author  : Aries
# @Site    : 
# @File    : py144_import_function.py
# @Software: PyCharm
'''
12-5 使用__import__()
    1.使用__import__()把一个模块导入到你的名称空间.你使用什么语法?
    2.使用__import__()从指定模块导入特定的名字
'''

if __name__ == '__main__':
    modules = __import__('mymodule')
    modules.foo()  # mymodule下的foo函数
    module1 = __import__('mymodule', fromlist=['foo'])
    foo = module1.foo
    foo()  # mymodule下的foo函数
