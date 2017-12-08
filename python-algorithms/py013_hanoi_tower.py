#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 上午11:31
# @Author  : Aries
# @Site    : 
# @File    : py013_hanoi_tower.py
# @Software: PyCharm

'''
汉诺塔
汉诺塔是印度一个古老传说的益智玩具。汉诺塔的移动也可以看做是递归函数。

我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，
首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
move(n, a, b, c)
例如，输入 move(2, ‘A’, ‘B’, ‘C’)，打印出：
A –> B
A –> C
B –> C
'''


def hanoi_tower(n, a, b, c):
    if n == 1:  # 如果只有一个盘子
        print '%s-->%s' % (a, c)
        return
    else:
        hanoi_tower(n - 1, a, c, b)  # 首先需要把 (N-1) 个圆盘移动到 b
        hanoi_tower(1, a, b, c)  # 将a的最后一个圆盘移动到c
        hanoi_tower(n - 1, b, a, c)  # 再将b的(N-1)个圆盘移动到c


hanoi_tower(2, 'A', 'B', 'C')
print '-' * 50
hanoi_tower(3, 'A', 'B', 'C')
