#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午6:06
# @Author  : Aries
# @Site    : 
# @File    : py044_finger_guessing_game.py
# @Software: PyCharm
'''
猜拳游戏
 随机数。设计一个“石头、剪子、布”游戏，有时又叫“Rochambeau”，你小时候可能玩过，下面是规则。
 你和你的对手，在同一时间做出特定的手势，必须是下面一种：石头、剪子、布。
 胜利者从下面的规则产生，这个规则本身是个悖论。
 (a)布包石头。
 (b)石头砸剪子。
 (c)剪子剪破布。
 在你的计算机版本中，用户输入他/她的选项，计算机找一个随机选项，然后由你的程序来决定一个胜利者或者平手。
 注意，最好的算法是尽量少使用if语句。
'''
import random

rochambeau = ['rock', 'scissor', 'cloth']

user_input = int(raw_input('1为石头rock,2为剪刀scissor,3为布cloth.请选择并输入对应的数字:\n'))

randomResult = rochambeau[random.randint(1, 3) - 1]

userResult = rochambeau[user_input - 1]  # 用户出拳


def myRochambeau(randomResult, userResult):
    if (randomResult == rochambeau[0] and userResult == rochambeau[2]) or \
            (randomResult == rochambeau[1] and userResult == rochambeau[0]) or \
            (randomResult == rochambeau[2] and userResult == rochambeau[1]):
        return '你赢了!'
    elif randomResult == userResult:
        return '平手!'
    else:
        return '你输了!'


print '你出了%s,程序出了%s,%s' % (userResult, randomResult, myRochambeau(randomResult, userResult))
