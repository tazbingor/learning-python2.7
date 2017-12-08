#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午6:27
# @Author  : Aries
# @Site    : 
# @File    : py107_functional_map_file.py
# @Software: PyCharm
'''
11-11.
用map()进行函数式编程。写一个使用文件名以及通过除去每行中所有排头和最尾的空白来“清洁”文件。
在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。
'''

import os


# 获得一个格式化后的文件行列表
def format_file_lines(filePath):
    # type: (str) -> list
    lines = get_file_lines(filePath)  # 打开文件,获得文件列表
    return map(lambda string: string.strip(), lines)


# 获得一个目标文件列表
def get_file_lines(dirPath, opt='rb'):
    # type: (str, str) -> list
    f = open(dirPath, opt)
    lines = f.readlines()
    f.close()
    return lines


# 写入文件
def write_in_file(resource, newPath, opt='wb'):
    # type: (str, str, str) ->  None
    # print resource
    f1 = open(newPath, opt)
    for i in resource:
        f1.write(i + '\n')
    f1.close()


# 删除文件
def delete_file(filepath):
    # type: (str) -> None
    if os.path.isfile(filepath):
        os.remove(filepath)


# 用户选项
def user_options(options):
    # 选择新文件还是覆盖旧的文件
    if options == 1:  # 写入新文件
        path_name = raw_input('请输入新的文件名:\n')
        write_in_file(FORMAT_LINES, path_name)

    elif options == 2:  # 覆盖旧文件
        delete_file(u'test.txt')
        user_options(3)

    else:
        write_in_file(FORMAT_LINES, u'test.txt')


# 启动脚本时就先保存格式化后的文件内容
FORMAT_LINES = format_file_lines(u'test.txt')


def main():
    # 用户选择读取方式
    user_input = int(raw_input('请选择你需要的操作: 1.复制源文件并创建新文件 2.修改后覆盖源文件\n'))
    user_options(user_input)


if __name__ == '__main__':
    main()
