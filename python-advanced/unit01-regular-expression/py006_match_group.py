#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/9 下午7:24
# @Author  : Aries
# @Site    : 
# @File    : py006_match_group.py
# @Software: PyCharm
'''
匹配分组
    |       匹配左右任意一个表达式
    (ab)    将括号中字符作为一个分组
    \num    引用分组num匹配到的字符串
    (?P<name>) 分组起别名
    (>P=name)  引用别名为name分组匹配到的字符串
'''
import re


def re_email(email):
    try:
        re_string = r'\w{4,20}@(163|qq|126|outlook)\.com$'
        return re.match(re_string, email).group()
    except AttributeError:
        return None


def re_html(code):
    try:
        re_string = r'<[A-Za-z]*>\w*</[A-Za-z]*>'
        return re.match(re_string, code).group()
    except AttributeError:
        return None


def re_html1(code):
    try:
        re_string = r'<(\w*)><(\w*)>.*</\2></\1>'
        return re.match(re_string, code).group()
    except AttributeError:
        return None


def re_html2(code):
    try:
        re_string = r'<(?P<name1>\w*)><(?P<name2>\w*)>' \
                    r'.*</(?P=name2)></(?P=name1)>'
        return re.match(re_string, code).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    # 匹配163,qq,126,outlook邮箱
    print re_email('python@outlook.com')  # python@outlook.com
    # 匹配<html>hh</html>
    print re_html('<html>hh</html>')  # <html>hh</html>

    # 匹配<html><h1>www.python.com</h1></html>
    print re_html1('<html><h1>www.python.com</h1></html>')  # <html><h1>www.python.com</h1></html>

    # 再次匹配<html><h1>www.python.com</h1></html>
    print re_html2('<html><h1>www.python.com</h1></html>')  # <html><h1>www.python.com</h1></html>
