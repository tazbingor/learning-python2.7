#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/26 下午6:28
# @Author  : Aries
# @Site    : 
# @File    : py126_dos_shell.py
# @Software: PyCharm
'''
13-14.DOS。
为DOS机器编写一个Unix操作界面的shell。
你向用户提供一个命令行，使得用户可以在那里输入unix命令，你可以对这些命令进行解释，并把返回相应的输出。

'''
import os


class Shell(object):
    def __init__(self):
        self.commands = {
            'ls': 'dir',
            'more': 'more',
            'cat': 'type',
            'cp': 'copy',
            'mv': 'ren',
            'rm': 'del'
        }

    def translate(self, cmd):
        opt = cmd.split()
        if opt[0] in self.commands:
            opt[0] = self.commands[opt[0]]
        return ' '.join(opt)

    def start(self):
        while 1:
            cmd = raw_input('#')
            cmd = self.translate(cmd)
            if cmd == 'exit':
                break
            else:
                os.system(cmd)


if __name__ == '__main__':
    dos_shell = Shell()
    dos_shell.start()
