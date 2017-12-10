#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/19 下午9:35
# @Author  : Aries
# @Site    : 
# @File    : py051_dict_and_list.py
# @Software: PyCharm
'''
列表和字典练习
(a) 创建一个字典，并把这个字典中的键按照字母顺序显示出来。 sorted(dict1)

(b) 现在根据已按照字母顺序排序好的键，显示出这个字典中的键和值。

(c)同(b),但这次是根据已按照字母顺序排序好的字典的值，显示出这个字典中的键和值。(注

意：对字典和哈希表来说，这样做一般没有什么实际意义，因为大多数访问和排序(如果需要)都是

基于字典的键，这里只把它作为一个练习。)


'''

# a , b
dict1 = {
    'p': 1,
    'y': 2,
    't': 3,
    'h': 4,
    'o': 8,
    'n': 8
}
for i in sorted(dict1):
    print i,
print
print '-' * 50

# c 按字典序显示key和value
for i in sorted(dict1):
    print i, ' : ', dict1[i]
print '-' * 50
