#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/7 下午7:46
# @Author  : Aries
# @Site    : 
# @File    : py025_number_pyramid.py
# @Software: PyCharm
'''
数字金字塔
public static void main(String[] args) {
  for (int i = 1; i <=7; i++) {
   for (int j = 7; j >i; j--) {
    System.out.print(" ");

   }
   for (int j = i; j >=1; j--) {
    System.out.print(j);

   }
   for (int j = 2; j <=i; j++) {
    System.out.print(j);

    }
   System.out.println();

   }

  }
'''

user_number = int(raw_input("请输入15以内的数字:\n"))
item = 1
while item <= user_number:
    num = user_number
    while num > item:  # 计算两边空格符的数量
        print ' ',
        num -= 1
    num = item
    while num >= 1:  # 计算金字塔左半边的数字
        print num,
        num -= 1

    num = 2
    while num <= item:  # 计算金字塔又半边的数字
        print num,
        num += 1

    item += 1
    print
