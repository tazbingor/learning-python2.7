#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 上午10:49
# @Author  : Aries
# @Site    : 
# @File    : py022_number_functions_random.py
# @Software: PyCharm
# random

# 记不记得dota美剧开盘会让玩家随机选择英雄的时候输入 -random?
# python 的内建函数random()于此功能相似
'''
猜随机数游戏
'''
import random

result = random.randint(1, 101)  # 整型随机数
# print result

while True:
    print "请输入你要猜的随机数\n"
    user_input = int(input())
    if (user_input == result):
        print "你猜对了!此随机出答案正是%s" % repr(result)
        break

    else:
        print "猜错了!"
        continue
