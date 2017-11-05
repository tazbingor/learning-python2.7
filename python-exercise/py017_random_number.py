#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/5 下午3:39
# @Author  : Aries
# @Site    : 
# @File    : py017_random_number.py
# @Software: PyCharm
# 求随机数
'''
生成一个随机数列表
1. 次列表由N个元素的随机数n组成
2. N的取值范围是 1 < N <=100
3. n的取值返回是 0 <= n <= 2**31  -1
4. 然后再从此列表中取出一个N( 1< N <= 100) 个元素存放至新的列表中
5. 打印这个子集
'''

import random

arr = []
for item in range(random.randint(1, 101)):
    arr.append(random.randint(0, (2 ** 30 - 1) * 2 + 1))
arr.sort()
print arr
