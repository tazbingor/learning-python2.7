#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/8 下午9:08
# @Author  : Aries
# @Site    : 
# @File    : py004_numerical.py
# @Software: PyCharm
'''
表示数量的正则

 *      匹配前一个字符出现0次或者无限次,即可有可无
 +      匹配前一个字符穿件一次或者无限次,即至少有一次
 ?      匹配前一个字符出现1次或者0次,要么又一次,要么没有
 {m}    匹配前一个字符串出现m次
 {m,}   匹配前一个字符至少出现m次
 {m,n}  匹配前一个字符至少出现m到n次
'''
import re


def re_password(pwd):
    re_string = '[a-zA-Z0-9_]{8,19}'
    try:
        result = re.match(re_string, pwd)
        return result.group()
    except AttributeError:
        return None


if __name__ == '__main__':
    re_string = '[A-Z][a-z]'
    result = re.match(re_string, 'Py')
    print result.group()  # Py

    re_string = '[A-Z][a-z]*'
    result = re.match(re_string, 'Python')
    print result.group()  # Python

    #  +      匹配前一个字符穿件一次或者无限次,即至少有一次
    re_string = '[a-zA-Z_]+[\W_]*'
    result = re.match(re_string, 'Python')
    print result.group()  # Python
    result = re.match(re_string, '_add')
    print result.group()  # _add
    result = re.match(re_string, 'showMenu')
    print result.group()  # showMenu

    #  ?      匹配前一个字符出现1次或者0次,要么又一次,要么没有
    re_string = '[1-9]?[0-9]'
    result = re.match(re_string, '9')
    print result.group()  # 9
    result = re.match(re_string, '09')
    print result.group()  # 0
    result = re.match(re_string, '999')
    print result.group()  # 99

    # 需求,匹配9-18位的密码,可以是大小写英文字母,数字,下划线
    print re_password('123134')  # None
    print re_password('thisispwd')  # thisispwd
