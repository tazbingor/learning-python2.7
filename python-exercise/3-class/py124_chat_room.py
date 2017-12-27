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


class message(object):
    melib = []

    def make_msg(self, me, nameto, namefrom):
        index = 0
        me1 = me + '   from   ' + namefrom
        li = [me1, nameto, index]
        self.melib.append(li)

    def check_msg(self, name):
        for i in self.melib:
            if i[1] == name and i[2] == 0:
                print i[0]
                i[2] = 1


class Room(object):
    _namelist = []
    _room_msg = []

    def __init__(self, name, user01, user02):
        self.roomname = name
        self._namelist.append(user01)
        self._namelist.append(user02)

    def add_msg(self, me, name):
        me1 = me + '  from  ' + name
        index = 0
        li = [me1, index]
        self._room_msg.append(li)

    def view_msg(self):
        for i in self._room_msg:
            if i[1] == 0:
                print i[0]
                i[1] = 1


class User(object):
    __user = []
    __roomlist = []

    def __init__(self, name):
        self.name = name
        self.__user.append(name)

    # 用户可以发送信息
    def send_msg(self, userto):
        if userto in self.__user:
            me = raw_input('message:')
            mes = message()
            mes.make_msg(me, userto, self.name)
        else:
            print 'no such user'

    # 用户接收信息
    def accepy_msg(self):
        mes = message()
        mes.check_msg(self.name)

    # 创建房间
    def create_room(self, username, roomname):
        ro = Room(roomname, username, self.name)
        self.__roomlist.append(ro)

    # 发信息
    def chat_room(self, roomname, mes):
        for i in self.__roomlist:
            if i.roomname == roomname:
                i.add_msg(mes, self.name)

    # 接收房间信息
    def view_room_msg(self, roomname):
        for i in self.__roomlist:
            if i.roomname == roomname:
                i.view_msg()


if __name__ == '__main__':
    u1 = User('张三')
    u2 = User('李四')
    u3 = User('王五')

    u1.create_room('李四', '房间1')
    u1.chat_room('房间1', '你好 李四')
    u1.create_room('王五', '房间2')
    u1.chat_room('房间2', '好久不见 王五')

    u2.view_room_msg('房间1')
    u3.view_room_msg('房间2')
    u2.chat_room('房间1', '李四??')
    u1.view_room_msg('房间1')
    u1.view_room_msg('房间2')
