#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午9:08
# @Author  : Aries
# @Site    : 
# @File    : py037_modify_dictionary.py
# @Software: PyCharm
'''
修改字典

'''

mydict = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}

# 1. 更新已有条目
mydict[2] = 'Half-Life 2'
mydict[4] = 'G Fat'
print mydict  # {8: 'eight', 2: 'Half-Life 2', 4: 'G Fat', 6: 'six'}

# 2. 增加条目
mydict[10] = 'Team Fortress 2'
print mydict  # {8: 'eight', 2: 'Half-Life 2', 4: 'G Fat', 10: 'Team Fortress 2', 6: 'six'}

# 3. 删除字典元素
del mydict[2]
print mydict  # {8: 'eight', 4: 'G Fat', 10: 'Team Fortress 2', 6: 'six'}
mydict.pop(4)
print mydict  # {8: 'eight', 10: 'Team Fortress 2', 6: 'six'}
