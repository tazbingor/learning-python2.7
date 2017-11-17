#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午7:31
# @Author  : Aries
# @Site    : 
# @File    : py032_tuple.py
# @Software: PyCharm
'''
python tuple 元组

元组的特点
1.若只访问元组中其中一个元素,那么返回也是该元素,切类型相同
2.若已切片访问元组,那么返回的也是一个元组
3.元组与字符串一样,不可变
'''

# 创建元组
num_tuple = (1, 2, 3, 4, 5, [0, 1])
print num_tuple

# 访问元组
print num_tuple[0]  # 1
print num_tuple[:4]  # (1, 2, 3, 4)
print type(num_tuple[0])  # <type 'int'>
print type(num_tuple[:4])  # <type 'tuple'>
# print num_tuple[5][0]  # 0
print num_tuple[5][1]  # 1

# 更新元组
num_tuple += (7, 8, 9)
print num_tuple  # (1, 2, 3, 4, 5, [0, 1], 7, 8, 9)
