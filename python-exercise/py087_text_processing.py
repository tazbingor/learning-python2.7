#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午6:39
# @Author  : Aries
# @Site    : 
# @File    : py087_text_processing.py
# @Software: PyCharm
'''
9–16. 文本处理.
人们输入的文字常常超过屏幕的最大宽度. 编写一个程序, 在一个文本文件中查找长度大于 80 个字符的文本行.
从最接近 80 个字符的单词断行, 把剩余文件插入到下一行处.程序执行完毕后, 应该没有超过 80 个字符的文本行了
ps:考虑一个中文字在python中的为3
'''
import os


def check_text():
    """文档处理函数，对长度超过80的进行截断"""
    f = open("1.txt", "r")
    lines_1 = f.readlines()
    f.close()
    lines_2 = []  # 将新生成的文档先储存在lines_2中
    for line in lines_1:
        if len(line) > 80:
            if line[80] == " ":  # 如果81个位置是空格，就不需要考虑单词边界问题
                lines_2.append(line[:80] + "n")
                lines_2.append(line[81:])
            else:
                local = line[:80].rfind(" ")  # 否则查找最靠近第80个位置的空格截断，保持单词的完整性
                lines_2.append(line[:local] + "n")
                lines_2.append(line[local + 1:])
        else:
            lines_2.append(line)
    f = open("1.txt", "w")
    f.writelines(lines_2)
    f.close()


if __name__ == "__main__":
    while True:  # 循环检测每行的长度，直至长度全部小鱼或等于80
        f = open("1.txt", "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            if len(line) > 80:
                check_text()
                break
        else:
            break
    print "Done!"
