#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/8 下午8:50
# @Author  : Aries
# @Site    : 
# @File    : py003_illustrate_matching.py
# @Software: PyCharm
'''
举例匹配
 []     匹配[]中举例的字符

'''
import re

if __name__ == '__main__':
    result = re.match('h', 'hello')
    print result.group()  # h

    result = re.match('H', 'Hello')
    print result.group()  # H

    # 兼容大小写
    re_string = '[Pp]'
    result = re.match(re_string, 'python')
    print result.group()  # p

    result = re.match(re_string, 'Python')
    print result.group()  # P

    # 匹配0-9
    result = re.match('[0-9][0-9][0-9][0-9][0-9]', '10086')
    print result.group()  # 10086
