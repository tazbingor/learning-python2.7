#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/31 上午11:31
# @Author  : Aries
# @Site    : 
# @File    : py004_recursion.py
# @Software: PyCharm

'''
递推算法
即通过已知条件，利用特定关系得出中间推论，直至得到结果的算法。
'''

# 递推算法解决一张大饼切100刀最多切多少块
# 1 + 1 + 2 + 3 + 4 + 5
arr = [item for item in range(1, 101)]  # 储存1 - 100 的元素
arr.insert(0, 1)
print arr


# print sum(arr)

# 实现一个sum函数
def mySum(arr):
    temp = 0
    for item in arr:
        temp += item
    return temp


print mySum(arr)
