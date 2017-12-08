#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午3:48
# @Author  : Aries
# @Site    : 
# @File    : py099_function_02.py
# @Software: PyCharm
'''
11-3 函数。
在这个练习中，我们将实现max()和min()内建函数。
(a) 写分别带两个元素返回一个较大和较小元素，简单的max2()和min2()函数。他们应该可以用任意的python 对象运作。
    举例来说，max2(4,8)和min2(4,8)会各自每次返回8 和4。
(b) 创建使用了在a 部分中的解来重构max()和min()的新函数my_max()和my_min().这些函数分别返回非空队列中一个最大和最小值。
    它们也能带一个参数集合作为输入。用数字和字符串来测试你的解。

'''


# a
def max2(x, y):
    if x > y:
        return x
    else:
        return y


max_2 = lambda x, y: x if x > y else y


def min2(x, y):
    if x < y:
        return x
    else:
        return y


min_2 = lambda x, y: x if x < y else y


# b
def myMax(*alist):
    res = alist[0]
    for i in alist:
        res = max_2(res, i)
    return res


def myMin(*alist):
    res = alist[0]
    for i in alist:
        res = min_2(res, i)
    return res


if __name__ == '__main__':
    # a
    print max2(4, 8)  # 8
    print max_2(4, 8)  # 8
    print min2(4, 8)  # 4
    print min_2(4, 8)  # 4
    print '-' * 50

    # b
    print myMax(2, 1, 8, 9, 11)  # 11
    print myMax('JS', 'Java', 'golang', 'c', 'python')  # python
    print myMin(2, 1, 8, 9, 11)  # 1
    print myMin('JS', 'Java', 'golang', 'c', 'python')  # Java
    print '-' * 50
