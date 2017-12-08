#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午3:28
# @Author  : Aries
# @Site    : 
# @File    : py097_parameter.py
# @Software: PyCharm
'''
11-1 参数。比较下面3个函数：
def countToFour1():
    for eachNum in range(5):
        print eachNum

def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum

def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum

给定如下的输入直到程序输出，你认为会发生什么？向下表11.2填入输出。
        如果你认为给定的输入会发生错误的话填入“ERROR”或者如果没有输出的话填入“NONE”。

    input           countToFour1()          countToFour2()          countToFour3()
      2                   ERROR                 NONE                     NONE
      4                   ERROR                 NONE                     NONE
      5                   ERROR                 NONE                     NONE
'''


def countToFour1():
    for eachNum in range(5):
        print eachNum


def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum


def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum


if __name__ == '__main__':
    # 2
    # countToFour1(2)  # TypeError: countToFour1() takes no arguments (1 given)
    countToFour2(2)
    countToFour3(2)
    print'-' * 50

    # 4
    # countToFour1(4)  # TypeError: countToFour1() takes no arguments (1 given)
    countToFour2(4)
    countToFour3(4)
    print'-' * 50

    # 5
    # countToFour1(5)  # TypeError: countToFour1() takes no arguments (1 given)
    countToFour2(5)
    countToFour3(5)
