#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/5 上午11:31
# @Author  : Aries
# @Site    : 
# @File    : py015_common_divisor.py
# @Software: PyCharm

# 求两个整数的最大公约数,和最小公倍数
# 最大公约数
def getCommonDivisor(number1, number2):
    temp = abs(number1 - number2)
    if (number1 % temp) == (number2 % temp) == 0:
        return temp
    else:
        return getCommonDivisor(number2, temp)


# 最小公倍数
def getCommonMultiple(number1, number2):
    temp = getCommonDivisor(number1, number2)
    return number1 * number2 / temp


user_number1 = int(raw_input("请输入数字1:\n"))
user_number2 = int(raw_input("请输入数字2:\n"))

print "%s和%s的最大公约数为:%s" % (str(user_number1), str(user_number2), str(getCommonDivisor(user_number1, user_number2)))
print "%s和%s的最小公倍数为:%s" % (str(user_number1), str(user_number2), str(getCommonMultiple(user_number1, user_number2)))
