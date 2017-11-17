#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/9 下午9:38
# @Author  : Aries
# @Site    :
# @File    : py024_string_split.py
# @Software: PyCharm
'''
字符串切割

'''
str = 'hello python'
print str[1:5]  # ello

# 也可以设置步长进行跳跃切割()
print str[1:8:2]  # el y

# 字符串修改, python的字符串不能修改,以下所谓修改,相当于重新创建一个新字符串
str2 = 'hello'
str2 = 'M' + str2[1:]
print str2  # Mello

'''
in的使用
'''

# num = 0
# while 'e' in str:
#     num += 1
#     print num

# i = 1
# while i in range(1, 100):
#     print i
#     i += 1
str3 = 'JavaScript'
print 'j' in str3  # False
print 'J' in str3  # True

