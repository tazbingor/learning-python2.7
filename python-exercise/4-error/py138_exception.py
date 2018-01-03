#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/3 下午6:37
# @Author  : Aries
# @Site    : 
# @File    : py138_exception.py
# @Software: PyCharm
'''
10-7. 异常 下面两代码段a,b有何区别?

a.
    try:
        statement_A
    except ...:
        ...
    else:
        statement_B

b.
    try:
        statement_A
        statement_B
    except ...:
        ...


'''

'''
若statement_A出现异常,那么(a)和(b)都不会执行statem_B
倘若statement_A未出现异常,那么(a)和(b)都会执行statement_B,但若在此情况下statement_B也出现异常
   那么(a)的异常会被上层调用者捕捉,而(b)会被except下捕获到异常并做处理 
'''
