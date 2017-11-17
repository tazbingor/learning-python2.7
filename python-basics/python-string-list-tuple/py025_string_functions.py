#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/9 下午10:14
# @Author  : Aries
# @Site    : 
# @File    : py025_string_functions.py
# @Software: PyCharm
import string

'''
python string 内建函数
'''

# 输出0-9
print string.digits
print type(string.digits)

# 输出小写的a-z
print string.lowercase
print type(string.lowercase)

# 输出空格符
print string.whitespace
print len(string.whitespace)  # 长度为6
print type(string.whitespace)

# 首字母大写
str1 = 'hello'
print str1.capitalize()  # Hello
print
# 返回一个居中的字符串,字符前后填充总数为width的空格,也可自定义填充其他字符
str2 = 'rich'
strNew = str2.center(8, '*')

print strNew
print len(strNew)
print

# 某字符在字符串中出现的次数
str3 = 'hello world'
print str3.count('o', 0)  # 2
print

# 判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
print str3.endswith('d')
print str3.endswith('b')  # False
print

# 把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
str4 = '\tnumber\tone\t'
print str4
print str4.expandtabs(1)

# 寻找字符串
str5 = 'summit'
print str5.find('s')  # 0
print str5.find('g')  # -1

# 另一种寻找字符串的方式
print str5.index('s')  # 0
# print str5.index('g') # 若不存在,则报错

print '-' * 50

str6 = '加勒比海盗5'
# 判断字符串中是否有字母和数字
print str6.isalnum()  # False
print 'wow 8.0'.isalnum()  # False
print '8'.isalnum()  # True

# 判断字符串中是否全部为字母
print 'WOODZ'.isalpha()  # True

# 是否只包含数字
print '10086'.isdigit()  # True

