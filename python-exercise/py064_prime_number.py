#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午2:35
# @Author  : Aries
# @Site    : 
# @File    : py064_prime_number.py
# @Software: PyCharm
'''
8.4 素数. 我们在本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个素
   数. 请把相关代码转换为一个返回值为布尔值的函数,函数名为isprime(). 如果输入的
   是一个素数,那么返回True,否则返回False.
'''


def isPrime(number):
    count = number / 2
    while count > 1:
        if number % count == 0:
            return False
        count -= 1
    else:
        return True


print isPrime(7)  # True
print isPrime(100)  # False
