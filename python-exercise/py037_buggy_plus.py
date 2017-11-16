#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午7:57
# @Author  : Aries
# @Site    : 
# @File    : py037_buggy_plus.py
# @Software: PyCharm

# 输入数字
num_str = raw_input('Enter a number:\n')

# 字符串转数字
num_num = int(num_str)

# 定义fac_list列表 , 以用户输入的数字+1位界限,将1到次界限内的所有数字存入列表
fac_list = range(1, num_num + 1)
print 'BEFORE:', fac_list

# 循环自增变量i
i = 0

'''
修改处
'''
temp = []

# 确定循环的次数
while i < len(fac_list):
    # 当用户输入的数能将列表类的[i]元素余尽时
    if num_num % fac_list[i] == 0:
        # del fac_list[i] # 利用列表持长度确定循环次数,但在循环时又修改列表长度,这种做法有风险
        temp.append(fac_list[i])

    # 自增
    i = i + 1

# 删除列表中不能被num_num余尽的数
for item in temp:
    fac_list.remove(item)


# 打印最后结果
print "AFTER:", fac_list
