#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午7:41
# @Author  : Aries
# @Site    : 
# @File    : py059_easy_math.py
# @Software: PyCharm
'''
算数游戏,可以随机选择算数加减法.通过函数add(),sub()等价+,-操作符,可以使用operator模块中找到
    随机选择数字和算数函数,显示问题,以及验证结果,在3次错误的尝试后以给出结果,等到用户输入一个正确但后便会继续运行
'''
# 导入模块
from operator import add, sub, mul
from random import randint, choice

# 全局变量
opts = {
    '+': add,
    '-': sub,
    '*': mul,
}
MAXTRIES = 2


def doprob():
    op = choice('+-*')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = opts[op](*nums)

    pr = '%d %s %d=' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input... try again'


def main():
    while True:
        doprob()
        try:
            opts = raw_input('Again?[y]').lower()
            if opts and opts[0] == 'n':
                break
        except(KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
