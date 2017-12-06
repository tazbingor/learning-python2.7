#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午9:17
# @Author  : Aries
# @Site    : 
# @File    : py061_anonymous_function.py
# @Software: PyCharm
'''
匿名函数 anonymous function

'''


# 示例 1
def result():
    return True


res = lambda: True

# 示例 2
add = lambda a, b: a + b

if __name__ == '__main__':
    # print result()  # True
    # print res()  # True
    print add  # <function <lambda> at 0x1099782a8>
    print type(add)  # <type 'function'>
    print add(4, 4)  # 8
