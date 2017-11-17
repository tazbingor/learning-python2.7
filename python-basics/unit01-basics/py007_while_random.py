#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/30 上午12:09
# @Author  : Aries
# @Site    : 
# @File    : py007_while_random.py
# @Software: PyCharm
import random

# 猜数字游戏
# 猜 0 - 100 以内的数字
random_number = random.randint(0, 100)
while True:
    print "请输入1-100间的数字\n"
    input_number = int(input())

    if input_number == random_number:
        print "你猜对了!\n"
    elif input_number > random_number:
        print "你猜的数大了!\n"
    elif input_number < random_number:
        print "你猜的数小了!\n"
    else:
        print "您输入的数超出范围了!\n"
