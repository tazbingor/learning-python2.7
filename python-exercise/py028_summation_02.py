#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/8 下午5:17
# @Author  : Aries
# @Site    : 
# @File    : py028_summation_02.py
# @Software: PyCharm

'''
编写 个程序, 成下 的算术 例。
1*8+1=9
12 * 8 + 2 = 98
123 * 8 + 3 = 987
1234 * 8 + 4 = 9876
12345 * 8 + 5 = 98765
123456 * 8 + 6 = 987654
1234567 * 8 + 7 = 9876543
12345678 * 8 + 8 = 98765432
123456789 * 8 + 9 = 987654321


12 为 num1
结果为 result
末尾加的数为 num2

(num1 += i) * 8 + (num2 +=1) = result

'''

num1, num2 = 0, 0
result, i = 0, 1
while i < 10:
    num1 = num1 * 10 + i
    num2 += 1
    # print num1
    # print num2
    result = num1 * 8 + num2
    print "%s * 8 + %s = %s" % (str(num1), str(num2), str(result))
    i += 1
