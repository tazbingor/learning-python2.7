#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午5:08
# @Author  : Aries
# @Site    : 
# @File    : py101_default_parameters.py
# @Software: PyCharm
'''
11-5. 默认参数。
更新你在练习5-7中创建的销售税脚本以便让销售税率不再是函数的必要参数。使用你的地方税率作为默认参数。

'''


def business_tax(pureprice, rate=0.10):
    return pureprice * rate


def main():
    print '计算明朝商业税'
    print business_tax(300)


if __name__ == '__main__':
    main()
