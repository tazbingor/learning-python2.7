#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/28 下午9:27
# @Author  : Aries
# @Site    : 
# @File    : py111-common-abnormal.py
# @Software: PyCharm
'''
python 中常见的异常
    1. 未声明变量 -- NameError
    2. 除数为9 -- ZeroDivisionError
    3. 语法错误 -- SyntaxError: invalid syntax
    4. 溢出错误 -- ndexError: list index out of range
    5. 请求字典中一个不存在的Key -- KeyError
    6. 输入/输出错误 -- IOError: [Errno 2] No such file or directory: 'something'
    7. 访问未知对象属性 -- AttributeError: 'xxx.xxx' object has no attribute 'xxx'

'''

if __name__ == '__main__':
    # 访问一个未声明的变量
    # print foo # NameError: name 'foo' is not defined

    # 除数为0
    # print 1 / 0  # ZeroDivisionError: integer division or modulo by zero

    # 语法错误
    # for i  # SyntaxError: invalid syntax

    # 溢出错误
    # aList = []
    # print aList[1] # IndexError: list index out of range

    # 请求一个不存在的Key
    # aDict = {'1': 1, '2': 2}
    # print aDict['3'] # KeyError: '3'

    # 输入/输出错误
    # f = open('something') # IOError: [Errno 2] No such file or directory: 'something'

    # 访问未知对象属性
    # mySysExit = SystemExit()
    # mySysExit.foo # AttributeError: 'exceptions.SystemExit' object has no attribute 'foo'

    pass
