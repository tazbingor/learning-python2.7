#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/5 下午4:24
# @Author  : Aries
# @Site    : 
# @File    : py020_summation.py
# @Software: PyCharm
'''
求和
 循环崁套的 式计算连续整数之和,要求输出结果如下。如果输 数5,输出连续5个 数字之和:
1=1
1+2 =3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15

'''


def strResult(arr, col, item):
    temp = " "
    arr.append(col)
    if item - col == 1:
        temp = str(col) + "=" + str(sum(arr))
    else:
        temp = str(col) + "+"
    return temp


num = int(raw_input("请输入数字\n"))
item = 1
while item <= num:
    item += 1
    col = 1
    arr = []
    while col < item:
        print strResult(arr, col, item),
        col += 1
    print
