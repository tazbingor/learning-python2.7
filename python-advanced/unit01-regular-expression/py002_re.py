#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/8 下午7:53
# @Author  : Aries
# @Site    : 
# @File    : py002_re.py
# @Software: PyCharm
'''
re模块操作

 .      匹配任意一个字符除了\n
 \d     匹配数字
 \D     匹配非数字
 \s     匹配空白(空格)和Tab
 \S     匹配非空白
 \w     匹配单词字符,即A-Z,a-z,0-9
 \W     匹配非单词字符

 []     匹配[]中举例的字符
'''
import re

if __name__ == '__main__':
    # 任意字符
    result = re.match('.', 'abc')
    print result
    print result.group()  # a
    result = re.match('...', 'abc')
    print result.group()  # abc

    # 匹配数字
    result = re.match('\d', '123')
    print result.group()  # 1
    result = re.match('\d\d', '123')
    print result.group()  # 12
    result = re.match('\d\d\d', '123')
    print result.group()  # 123

    # 匹配非数字
    result = re.match('\D', 'ZOO')
    print result.group()  # Z
    result = re.match('\D\D', 'ZOO')
    print result.group()  # ZO
    result = re.match('\D\D\D', 'ZOO')
    print result.group()  # ZOO

    # 匹配空白
    result = re.match('\s', ' 23')
    print result.group()  #
    result = re.match('\s\d', ' 23')
    print result.group()  # 2
    result = re.match('\s\d\S', ' 23')
    print result.group()  # 23

    # 匹配非空白
    result = re.match('\w\w\w\w', 'Java')
    print result.group()  # Java
    result = re.match('\W\W\W\W\W\W\W\W\W\W\W\W', '你好世界')
    print result.group()  # 你好世界
