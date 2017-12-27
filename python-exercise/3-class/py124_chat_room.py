#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/26 下午3:48
# @Author  : Aries
# @Site    : 
# @File    : py124_chat_room.py
# @Software: PyCharm
'''
13-12.聊天室。
你需要三个类：
    一个Message类，它包含一个消息字符串以及诸如广播、单方收件人等其他信息。
    一个User类，包含了进入你聊天室的某个人的所有信息。
    一个Room类，它体现了一个更加复杂的聊天系统，用户可以在聊天时创建单独的房间，并邀请其他人加入。
'''


class Message(object):
    def __init__(self, message, recipients):
        self.msg = message
        self.recip = recipients


class User(object):
    def __init__(self, name='admin', sex='女', age=18):
        self.username = name
        self.usersex = sex
        self.age = age


class Room(object):
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2


if __name__ == '__main__':
    pass
