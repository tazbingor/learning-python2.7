#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午9:08
# @Author  : Aries
# @Site    : 
# @File    : py038_number_translate.py
# @Software: PyCharm
'''
数字翻译
列表。给出一个整型值，返回代表该值得英文，比如输入89会返回“eight-nine”。
附加题：能够返回符合英文语法规律的形式，比如输入89会返回“eighty-nine”。本练习中的值假定在0~1000。
'''

# 0 - 10
unitNumber = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
# 11 - 19
teenNumber = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# 20.30.40..90
tensDigit = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundred = 'hundred'
thousand = 'thousand'


def getDigitalEnglish(num):
    result = ''
    if num <= 10:
        result = unitNumber[num]
    elif 10 < num < 20:
        result = teenNumber[num - 11]
    elif 20 < num < 100:
        num_list = list(str(num))

        if num % 10 != 0:
            result = teenNumber[int(num_list[0]) - 1] + '-' + unitNumber[int(num_list[1])]
        else:
            result = tensDigit[num % 10 - 3]

    elif 100 < num <= 999:
        num_list = list(str(num))
        str1 = unitNumber[int(num_list[0])] + ' ' + hundred
        result = str1 + ' and ' + getDigitalEnglish(num % 100)
    elif num == 100:
        result = unitNumber[1] + ' ' + hundred

    elif num == 1000:
        result = unitNumber[1] + ' ' + thousand

    return result


# 用户输入
user_input = int(raw_input('请输入0到1000的数字:\n'))
print '%s的英文翻译为:%s' % (str(user_input), getDigitalEnglish(user_input))
