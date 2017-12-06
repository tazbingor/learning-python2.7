#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午9:31
# @Author  : Aries
# @Site    : 
# @File    : py062_pass_parameter.py
# @Software: PyCharm
'''
传递参数
    1.在python中,所有的对象都是通过引用来传递,函数也是如此,所以函数拥有其他的'别名'也是可以的
'''


def apple():
    print 'apple'


def fruits(func):
    func()


if __name__ == '__main__':
    # 1. 函数的'别名'
    yantai_apple = apple
    apple()  # apple
    yantai_apple()  # apple

    # 2. 将函数作为参数进行传递
    fruits(apple)  # apple
