#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午10:43
# @Author  : Aries
# @Site    : 
# @File    : py075_closure_03_decorator.py
# @Software: PyCharm
'''
闭包,装饰器的应用
'''

from time import time


def logged(when):
    # 日志写入函数
    def log(f, *args, **kargs):
        print '''Called:
        function: %s
        args: %r 
        kargs: %r''' % (f, args, kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)

        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print '\t\ttime delta: %s' % (time() - now)

        return wrapper

    try:
        return {
            'pre': pre_logged,
            'post': post_logged
        }[when]

    except KeyError, e:
        raise ValueError(e), 'must be \"pre\" or \"post\"'


@logged('post')
def hello(name):
    print 'Hello,', name


hello('World!')
