#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午4:41
# @Author  : Aries
# @Site    : 
# @File    : py030_list_sequence.py
# @Software: PyCharm
'''
序列类型函数
'''

# min 和 max
str_list = ['Woodz', 'Moon', 'Andy', 'Billy']
print min(str_list)  # Andy
print max(str_list)  # Woodz
print
str_list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print min(str_list1)  # a
print max(str_list1)  # g
# list比较字符串列表时,也是依照字典序进行排列
print

# sorted 和 reversed
arr = [1, 2, 3, 4]
for i in reversed(arr):  # 逆序
    print i
print sorted(arr)
print sorted(str_list)  # 依旧使用字典序进行排序
print

# enumerate 枚举
# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
test_list = ['魑', '魅', '魍', '魉']
for i, item in enumerate(test_list):
    print i, item

print
# 也可以自定义从几号开始
for i, item in enumerate(test_list, 1):  # 从1开始,并非从1元素下标开始
    print i, item
print

# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
# 然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
# 利用*号操作符，可以将list unzip（解压）

num_list1 = [1, 2]
num_list2 = [3, 4]
print zip(num_list1, num_list2)  # [(1, 3), (2, 4)]
num_list3 = [3, 4, 5]
print zip(num_list1, num_list3)  # [(1, 3), (2, 4)]

# sum()
# 列表内元素之和
print sum(num_list1)  # 3
print sum(num_list2)  # 7
# str_list2 = ['1', '2', '3', '4']
# print sum(str_list2)
print

# list() 与 tuple()
test_list1 = [1, 2, 3, 4]
test_tuple = tuple(test_list1)
print test_tuple  # (1, 2, 3, 4)
print test_tuple == tuple(test_list1)  # True
print
print test_list1 == list(test_tuple)  # True
print list(test_tuple)  # [1, 2, 3, 4]
