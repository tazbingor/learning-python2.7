#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/31 下午7:16
# @Author  : Aries
# @Site    : 
# @File    : py002_read_text_file.py
# @Software: PyCharm
# 读取文件并显示

# 获取文件名
file_name = raw_input("请输入想要打开的目标文件名: ")
# print type(file_name)
print

# 打开目标文件
file_obj = open(file_name, 'r')  # 读取文件
# print type(file_obj)
# print file_obj

for each_line in file_obj:
    print each_line
file_obj.close()
