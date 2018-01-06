#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午8:48
# @Author  : Aries
# @Site    : 
# @File    : py145_expand_import.py
# @Software: PyCharm
'''
12-6 扩展导入.创建一个 importAs() 函数.
这个函数可以把一个模块导入到你的名称空间, 但使用你指定的名字, 而不是原始名字。
例如:
    调用 newname=importAs('mymodule') 会导入mymodule ,
    但模块和它的所有元素都通过新名称 newname 或 newname.attr 访问。
这是 Python2.0 引入的扩展导入实现的功能。
'''


def importAs(name):
    return __import__(name)


if __name__ == '__main__':
    new_module = importAs('mymodule')
    new_module.foo()  # mymodule下的foo函数
