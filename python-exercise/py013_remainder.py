#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午4:10
# @Author  : Aries
# @Site    : 
# @File    : py013_remainder.py
# @Software: PyCharm
# 取余

'''
求出0-20之间的所有偶数
'''
even_numbers = []
for even_number in range(1, 21):
    if even_number % 2 == 0:
        even_numbers.append(even_number)
print even_numbers

'''
同上,输出所有奇数
'''
odd_numbers = []
for odd_number in range(1, 21):
    if odd_number % 2 != 0:
        odd_numbers.append(odd_number)
print  odd_numbers

'''
写一个函数,比较两个用户输入的整型,看两者之间是否存在整除关系,存在则为True,反之亦然
'''
user_number1 = int(input("请用户输入第一个整型数:\n"))
user_number2 = int(input("请用户输入第二个整型数:\n"))


def whetherNumberRemainder(number1, number2):
    if number1 % number2 == 0 or number2 % number1 == 0:
        return True
    else:
        return False


print "输入的两个数是否存在整除关系?结果为:%s" % str(whetherNumberRemainder(user_number1, user_number2))
