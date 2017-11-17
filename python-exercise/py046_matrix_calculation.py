#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午7:40
# @Author  : Aries
# @Site    : 
# @File    : py046_matrix_calculation.py
# @Software: PyCharm

# 矩阵相乘

import numpy

M = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
N = [[1, 1], [1, 1], [1, 1]]
result = [[0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(len(M)):
    for j in range(2):
        sum = 0
        for k in range(len(N)):
            sum += M[i][k] * N[k][j]
            result[i][j] = sum
print result

print '-' * 50

# 矩阵相加
X = [[10, 9, 6],
     [6, 1, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):  # 迭代输出行
    for j in range(len(X[0])):  # 迭代输出列
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print r
