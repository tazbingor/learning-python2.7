#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/28 上午11:24
# @Author  : Aries
# @Site    : 
# @File    : py001-bqmj.py
# @Software: PyCharm
# 百钱买鸡问题

# 公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，
# 用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。
if __name__ == '__main__':
    for gongJi in range(21):  # 100块钱能买20只公鸡
        for muJi in range(34):  # 100块钱能买34母鸡
            for xiaoJi in range(3, 301, 3):
                if gongJi * 5 + muJi * 3 + xiaoJi / 3 == 100 and \
                                                gongJi + muJi + xiaoJi == 100 and \
                                gongJi != 0 and muJi != 0 and xiaoJi != 0:
                    print "公鸡买:%s只, 母鸡买:%s只, 小鸡买:%s只;" % (str(gongJi), str(muJi), str(xiaoJi))
