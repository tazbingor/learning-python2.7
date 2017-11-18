#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/18 下午9:51
# @Author  : Aries
# @Site    : 
# @File    : py039_dictionary_functions.py
# @Software: PyCharm
'''
字典内建方法
'''

dict1 = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}

# 排序 sorted
print sorted(dict1)  # [2, 4, 6, 8] 排序了key
# 迭代输出
for eachKey in sorted(dict1):
    print dict1[eachKey]

# 更新字典 update()
dict2 = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}
dict3 = {
    10: 'ten',
    12: 'twelve'
}
dict2.update(dict3)
print dict2  # {2: 'two', 4: 'four', 6: 'six', 8: 'eight', 10: 'ten', 12: 'twelve'}

# 删除字典所有条目 clear()
dict3.clear()
print dict3  # {}

# 字典浅拷贝 copy() 返回原字典的副本
dict4 = dict3.copy()
print dict4  # {}

# 使用字典中的key找对应的value, get() 若没有则返回 NoneType
dict5 = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}
print dict5.get(2)  # two
print dict5.get('eight')  # None
print type(dict5.get('eight'))  # <type 'NoneType'>
print dict5.get(10)  # None

# 检测字典中是否含有某个元素 setdefault() 和 get类似,但setdefault()可以修改指定元素
# 倘若setdefault为检测出key和value,那么他会将你输入的键值对加入这个字典中
print dict5.setdefault(8)  # eight
print dict5.setdefault(10)  # None

print dict5.setdefault(2, '2')
temp = dict5.setdefault('two', '2')
print temp
print type(dict5.setdefault('two', '2'))  # <type 'str'>
print dict5  # {2: 'two', 4: 'four', 6: 'six', 8: 'eight', 10: None, 'two': '2'}
