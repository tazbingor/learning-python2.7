#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/7 下午4:08
# @Author  : Aries
# @Site    : 
# @File    : py021_multiplication_table.py
# @Software: PyCharm

'''
 for循环打印9*9乘法表,要求输出格式如下。

1     2   3   4   5   6   7   8   9
-----------------------------------
1|1   2   3   4   5   6   7   8   9
2|2   4   6   8   10  12  14  16  18
........
'''

print '\t1   2   3   4   5   6   7   8   9'
print '-' * 40

for i in range(1, 10, 1):
    print str(i) + '|',
    for j in range(1, 10, 1):
        print str(i * j) + "\t",
    print
