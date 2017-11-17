#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午2:59
# @Author  : Aries
# @Site    : 
# @File    : py015_dir.py
# @Software: PyCharm
'''
dir() 显示对象的属性,如果没有参数,则返回全局变量的名字
dir()返回的是一个列表类型
可以理解为查字典
'''

print type(dir(1))
print type(dir("漫步云端"))

# print dir("云中漫步")

book = "云中漫步"

# print dir(book)

import time

print dir(time)

print dir(time.time())
