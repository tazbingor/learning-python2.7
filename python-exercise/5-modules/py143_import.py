#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午8:37
# @Author  : Aries
# @Site    : 
# @File    : py143_import.py
# @Software: PyCharm
'''
12-3 导入'import module' 和 'from module import *'有何异同?

'''
# 以上题举例
import mymodule  # 绝对导入
from mymodule import foo  # 相对导入

if __name__ == '__main__':
    mymodule.foo()  # mymodule下的foo函数
    foo()  # mymodule下的foo函数
'''
很明显
如果采用from module import *,则可在代码中直接使用方法名
如果采用import module，则在代码中必须写成module.function的形式
'''

'''
12-4. 名称空间和变量作用域。名称空间和变量作用域有什么不同？

名称空间是纯粹意义上的名字和对象间的映射关系，而作用域还指出了从用户代码的哪些物理位置可以访问到这些名字。

'''
