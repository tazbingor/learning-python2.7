#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午7:10
# @Author  : Aries
# @Site    : 
# @File    : py161_match_card_number.py
# @Software: PyCharm
'''
15-15 在15.2小节里，我们给出一个匹配信用卡卡号的模式：[0-9]{15,16}。
但这个模式不允许用连字符号分割卡号中的数字。
请写出一个允许使用连字符的正则表达式，但要求连字符必须出现在正确的位置。
例如，15位卡号的格式是4-6-5，16位卡号的格式是4-4-4-4，位数不足时，添0补位。

'''
import re


def match_calendar(string=''):
    try:
        regex = r'^\d{4}[-| ](\d{6}[-| ]\d{0,5}|\d{4}[-| ]\d{4}[-| ]\d{0,4})$'
        return re.match(regex, string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_calendar('1234-567890-12345')  # 1234-567890-12345
    print match_calendar('1234-1234-1234-1234')  # 1234-1234-1234-1234
