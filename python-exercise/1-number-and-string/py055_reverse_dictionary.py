#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/20 下午4:46
# @Author  : Aries
# @Site    : 
# @File    : py055_reverse_dictionary.py
# @Software: PyCharm
'''
颠倒字典

颠倒字典中的键和值。用一个字典做输入，输出另一个字典，用前者的键做值，前者的值做键.
'''

# 使用压缩器
dict1 = {
    1: 'Java',
    2: 'Python',
    3: 'JavaScript'
}
dict1 = dict(zip(dict1.values(), dict1.keys()))
print dict1  # {'Python': 2, 'JavaScript': 3, 'Java': 1}

# 字典迭代
dict2 = {
    1: 'Java',
    2: 'Python',
    3: 'JavaScript'
}
dict2 = {value: key for key, value in dict2.items()}
print dict2  # {'Python': 2, 'JavaScript': 3, 'Java': 1}
