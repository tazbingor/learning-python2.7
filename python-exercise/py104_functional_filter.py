#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午5:35
# @Author  : Aries
# @Site    : 
# @File    : py104_functional_filter.py
# @Software: PyCharm
'''
11–8. 用filter()进行函数式编程.
使用练习5-4 你给出的代码来决定闰年。更新你的代码一边他成为一个函数如果你还没有那么做的话。
然后写一段代码来给出一个年份的列表并返回一个只有闰年的列表。然后将它转化为用列表解析。

'''


# 一般func
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:

            if year % 400 == 0:  # 世纪年闰年
                return True
            else:
                return False
        else:
            return True
    else:
        return False


leap_year_list = lambda years: [i for i in filter(isLeapYear, years)]


def main():
    years = [year for year in range(1000, 2018)]
    print isLeapYear(1000)
    print leap_year_list(leap_year_list(years))


if __name__ == '__main__':
    main()
