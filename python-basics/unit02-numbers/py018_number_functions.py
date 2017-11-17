#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午4:41
# @Author  : Aries
# @Site    : 
# @File    : py018_number_functions.py
# @Software: PyCharm
'''
数字内建函数
'''

# 四种数字类型的转换
print int(16.04)  # 16
print long(16l)  # 16
print float(16)  # 16.0
print complex(16.6)  # (16.6+0j)
print complex(16)  # (16.6+0j)

'''
数字功能函数
'''

'''abs() 绝对值'''
print abs(-100)  # 100
print abs(1.2j + 1.2j)  # 2.4
print abs(1.2 - 2.1j)  # 2.41867732449

'''
coerce()
如果有一个操作数是复数， 另一个操作数被转换为复数。  
否则，如果有一个操作数是浮点数， 另一个操作数被转换为浮点数。  
否则, 如果有一个操作数是长整数，则另一个操作数被转换为长整数；  
否则，两者必然都是普通整数，无须类型转换
'''
print coerce(1.0, 1)  # (1.0, 1.0)
print coerce(1, 1.0)  # (1.0, 1.0)
print coerce(100l, 1)  # (100L, 1L)
print coerce(100l, 1.0)  # (100.0, 1.0)
print coerce(10, 10)  # (10, 10)

'''
divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
某些情况下可以代替除法
'''
print divmod(7, 3)  # (2, 1)
print divmod(9, 3)  # (3 ,0)
print divmod(25, 10)  # (2, 5)
print divmod(2.5, 10)  # (0.0, 2.5)

'''
pow() 指数运算 ,其中第三个参数是%运算
'''
print 5 ** 2  # 25
print pow(5, 2)  # 25
print pow(5, 2, 2)  # 1

'''
round() 对浮点数四舍五入的运算,返回浮点数
其中第二个参数是指定四舍五入精确到几位
'''
print round(4.56)  # 5.0
print round(4.45)  # 4.0
print round(4.45, 1)  # 4.5
