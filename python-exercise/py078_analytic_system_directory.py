#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/29 下午7:40
# @Author  : Aries
# @Site    : 
# @File    : py078_analytic_system_directory.py
# @Software: PyCharm
'''
9-7 系统解析系统配置文件

'''

import platform  # 确定当前操作系统

sys = platform.system()
# print sys
if sys == 'Windows':
    pass

elif sys == 'Linux':
    pass

elif sys == 'MacOS':
    pass

print dir(sys)