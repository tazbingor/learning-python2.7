#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/15 上午2:03
# @Author  : Aries
# @Site    : 
# @File    : py034_copy.py
# @Software: PyCharm
import copy

'''
python copy 拷贝对象

1. 首先,在python中，对象赋值实际上都是进行对象引用（内存地址）传递
当创建一个对象，然后把它赋给另一个变量的时候，python并没有拷贝这个对象，而只是拷贝了这个对象的引用
2. 浅拷贝是相当于创建一个全新的对象,但修改了新对象后依然能影响原对象,本质上还是对原对象的引用
3. 深拷贝跟浅拷贝类似，深拷贝也会创建一个新的对象,并重新开辟一块新的内存已提供引用,再如何修改新对象也不会影响到原对象了

'''
# 变量赋值
a = '1'
b = a
print a is b
print id(a)
print id(b)

# 1. 对象赋值
woodz = ['student', 16, ['wow', 'war3', 'cs']]
billy = woodz
# 在查看它们俩是否都是相等id
print [id(i) for i in woodz, billy]
# 修改第二个对象,查看第一个对象是否有变化
billy[2].append('programming')
print billy
print woodz  # 都被修改

print '-' * 50

# 2.浅拷贝
woodz = ['student', 16, ['wow', 'war3', 'cs']]
billy = copy.copy(woodz)
print [id(i) for i in woodz, billy]  # 此时的id发生了变化,两不相同了
# 同样修改第二个对象,对比第一个
billy[2].append('communicate')
print billy
print woodz  # 依旧被同时修改了
print billy == woodz
print billy is woodz
print '-' * 50
# 使用切片操作再比较
woodz = ['student', 16, ['wow', 'war3', 'cs']]
billy = woodz[:]
print [id(i) for i in woodz, billy]  # id也发生了变化,两不相同
# 同样修改第二个对象,对比第一个
billy[2].append('communicate')
print billy
print woodz  # 依旧被同时修改了
print '-' * 50

# 使用工厂函数list()等
woodz = ['student', 16, ['wow', 'war3', 'cs']]
billy = list(woodz)
print id(woodz) == id(billy)
billy[2].append('Python')
print billy
print woodz  # 还是改变了
print '-' * 50

# 深拷贝 使用deepcopy
woodz = ['student', 16, ['wow', 'war3', 'cs']]
billy = copy.deepcopy(woodz)
print id(woodz) == id(billy)  # False
billy[2].append('Python')
print billy
print woodz  # 没有影响到原来的对象
