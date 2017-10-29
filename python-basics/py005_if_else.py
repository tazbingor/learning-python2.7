#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/29 上午11:10
# @Author  : Aries
# @Site    : 
# @File    : py005_if_else.py
# @Software: PyCharm

# if else elif 控制语句

# 输入分数,显示成绩
print "请输入分数:"
score = int(input())
if score > 80 and score <= 100:
    print "优"
elif score >= 60 and score <= 80:
    print "良"
elif score >= 0 and score < 60:
    print "不及格"
else:
    print "你超纲了!"
