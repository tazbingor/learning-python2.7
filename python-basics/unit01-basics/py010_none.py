#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 上午9:55
# @Author  : Aries
# @Site    : 
# @File    : py010_none.py
# @Software: PyCharm
# 核心笔记 布尔值

'''
python中的虽有标准对象都是可以进行bool测试的
'''

# None
print bool(None)
print None == None  # True

# 布尔型
# 以及所有为零的数
print bool(0)
print bool(0.0)
print bool(0L)
print bool(0.0j)

# 空字符串
print bool("")

# 空列表
print bool([])
# 空元组
print bool(())
# 空字典
print bool({})
