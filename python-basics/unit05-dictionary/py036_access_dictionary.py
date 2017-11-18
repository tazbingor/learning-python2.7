#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午8:48
# @Author  : Aries
# @Site    : 
# @File    : py036_access_dictionary.py
# @Software: PyCharm
'''
访问字典
'''

# 1 .遍历字典,使用key()
mydict = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}
for key in mydict.keys():
    print key, ',', mydict[key]  # 若为了得到字典中的某个值,可以用[]方式得到

print '-' * 50

# 2. 使用迭代器遍历字典
for key in mydict:
    print key, ',', mydict[key]

print '-' * 50

# 3. 确定某元组在当前字典中
print 'two' in mydict
print 2 not in mydict
print 9 in mydict
print 2 in mydict  # True
print 'two' in mydict.keys()
print 'two' in mydict.values()  # True
print mydict.has_key(2)  # True

print '-' * 50

