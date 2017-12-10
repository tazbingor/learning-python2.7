#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午12:43
# @Author  : Aries
# @Site    :
# @File    : py006_exam_results.py
# @Software: PyCharm

# 考试成绩

student_arr = {
    'bill': 80,
    'woodz': 90,
    'tazdingo': 99,
    'webber': 60,
    'billy': 70
}

# print dir(student_arr)

for key, value in student_arr.items():
    result = ''
    if 90 <= value <= 100:
        result = 'A'
    elif 80 <= value <= 89:
        result = 'B'
    elif 70 <= value <= 79:
        result = 'C'
    elif 60 <= value <= 69:
        result = 'D'
    elif 0 < value < 60:
        result = 'F'
    else:
        result = 'Z'
    print repr(key) + "考试分数为\t:" + repr(value) + ",考试成绩为:" + result
