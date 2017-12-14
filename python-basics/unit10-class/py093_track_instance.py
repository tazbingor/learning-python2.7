#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/14 下午7:15
# @Author  : Aries
# @Site    : 
# @File    : py093_track_instance.py
# @Software: PyCharm
'''
跟踪实例
'''


class InstTrack(object):
    count = 0

    def __init__(self):
        InstTrack.count += 1

    def __del__(self):
        InstTrack.count -= 1

    def howMany(self):
        return InstTrack.count


if __name__ == '__main__':
    a = InstTrack()
    b = InstTrack()
    print b.howMany()  # 2
    print a.howMany()  # 2
    del a
    print InstTrack.count  # 1
