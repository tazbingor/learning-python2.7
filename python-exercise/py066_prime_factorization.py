#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午4:14
# @Author  : Aries
# @Site    : 
# @File    : py066_prime_factorization.py
# @Software: PyCharm
'''
8.6 素因子分解. 以刚才练习中的isprime()和getfactors()函数为基础编写一个函数,它接受
   一个整型作为参数,返回该整型所有素数因子的列表.这个过程叫做求素因子分解,它输出
   的所有因子之积应该是原来的数.注意列表里可能有重复的元素.例如输入20,返回结果应该
   是[2,2,5].
'''


# 判断素数
def isPrime(number):
    count = number / 2
    while count > 1:
        if number % count == 0:
            return False
        count -= 1
    else:
        return True


# 因数
def getFactor(number):
    fList = [1]
    for i in range(1, number + 1):
        if number % 2 == 0:
            fList.append(2)
            number = number / 2
        else:
            fList.append(number)
            break
    return fList


def primeFactors(number):
    if isPrime(number):
        return [1, number]
    else:
        return getFactor(number)


num = int(raw_input('请输入数字:\n'))
print primeFactors(num)
