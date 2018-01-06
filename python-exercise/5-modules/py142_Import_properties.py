#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午8:22
# @Author  : Aries
# @Site    : 
# @File    : py142_Import_properties.py
# @Software: PyCharm
'''
12-2. 导入属性.假设你的模块mymodule中有一个foo()函数:
    1.把这个函数导入到你的命名空间有哪两种方法?
    2.这两种方法有何异同?

'''
import mymodule  # 绝对导入
from mymodule import foo  # 相对导入

if __name__ == '__main__':
    mymodule.foo()  # mymodule下的foo函数
    foo()  # mymodule下的foo函数

'''
1.导入命名空间的方法有绝对导入和相对导入
2.绝对导入,使用'import 空间名称' 的方式,将mymodule内的属性全部导入.
  相对导入,使用'from 属性/函数名 import 空间名'的方式,只是导入mymodule中的foo函数
'''
