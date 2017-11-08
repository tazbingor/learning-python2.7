#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/8 下午5:47
# @Author  : Aries
# @Site    : 
# @File    : py030_true_and_false.py
# @Software: PyCharm

'''
 在空白处填上True或False
p      q    (not p) or q    (p and q) or q      (p or q) and p      (p or q) and (p and q)
True True       True            True                True                    True
True False      False           False               True                    False
False True      True            True                False                   False
False False     True            False               False                   False


'''

p = True
q = True
print not p  # False
print (not p) or q  # True
print (p and q) or q
print (p or q) and p
print (p or q) and (p and q)

print '--' * 30

p = True
q = False
print (not p) or q
print (p and q) or q
print (p or q) and p
print (p or q) and (p and q)

print '--' * 30

p = False
q = True
print (not p) or q
print (p and q) or q
print (p or q) and p
print (p or q) and (p and q)

print '--' * 30

p = False
q = False
print (not p) or q
print (p and q) or q
print (p or q) and p
print (p or q) and (p and q)
