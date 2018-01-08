#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/2 下午8:00
# @Author  : Aries
# @Site    : 
# @File    : py116_raise.py
# @Software: PyCharm
'''
raise语句 主动抛出异常
'''


def thorw_error():
    raise Exception("抛出一个异常")


if __name__ == '__main__':
    thorw_error()

'''
Traceback (most recent call last):
  File "project/PycharmProjects/rising-python-classics/python-basics/unit11-error/py116_raise.py", line 18, in <module>
    thorw_error()
  File "project/PycharmProjects/rising-python-classics/python-basics/unit11-error/py116_raise.py", line 14, in thorw_error
    raise Exception("抛出一个异常")
Exception: 抛出一个异常
'''
