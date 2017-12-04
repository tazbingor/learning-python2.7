#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午3:50
# @Author  : Aries
# @Site    : 
# @File    : py085_record_result.py
# @Software: PyCharm
'''
9-14 记录结果。修改你的计算器程序（练习5-6）使之接受命令行参数。例如$ calc.py 1 + 2 只输出计算结果。
另外，把每个表达式和它的结果写入到一个磁盘文件中，当使用下面的命令时 $ calc.py print 会把记录的内容显示到屏幕上，然后重置文件。
这里是样例展示：
$ calc.py 1 + 2
3
$ calc.py 3 ^ 3
27
$ calc.py print
1 + 2
3
3 ^ 3
27
$ calc.py print
$

'''

# 1. 字符串的切割
# 2. 打开文件
# 3. 计算后写入文件
#    3.1 操作步骤写入文件
#    3.2 结果写入文件

opts = ['+', '-', '*', '/', '^', '%']


# 计算函数
def num_calculator(num1, num2, opt):
    # print num1, ',', num2, ',', opt
    # print len(num1), ':', type(num1)
    # print len(num2), ':', type(num2)
    # print len(opt), ':', type(opt)
    # print num1 + opt + num2
    # print eval(num1 + opt + num2)
    # print 3^3
    return eval(str(num1).strip() + str(opt) + str(num2).strip())


# 返回字符串末尾下标
def get_index(user_str, suffix):
    return user_str.find(suffix) + len(suffix)


# 获取结果
def get_result(user_str):
    string = str(user_str[get_index(user_str, '.py'):]).replace(' ', '')
    num1 = 0
    opt = ''
    num2 = 0
    for i in range(len(string)):
        for j in range(len(opts)):
            if string[i] == opts[j]:
                num1 = string[:i]
                opt = string[i]
                num2 = string[i + 1:]
                print num1, ' ', opt, ' ', num2
                return num_calculator(num1, num2, opt)


opts = ['+', '-', '*', '/', '^', '%']

if __name__ == '__main__':

    count = 0  # 操作标记

    user_input = raw_input("命令行计算器,请输入计算的条目(如 calc.py 1 + 2,则显示3):\n")
    user_str = user_input.strip()
    file_path = user_str[:get_index(user_str, '.py')]
    file1 = open(file_path, 'w')

    code = user_str[get_index(user_str, '.py'):]
    # 写入操作和结果至文件中

    while True:
        if code.strip() == 'print':
            # print code
            print file1.readlines()
            if count > 0:
                for line in file1:
                    print line
                count += 1
            else:
                # 清空文件
                file1.truncate()  # 清空文件内容
                continue
        else:
            # 切割字符串找到,文件名,数字一,opt,数字2
            result = get_result(user_str)
            for i in [user_str, result]:
                file1.write(str(i))
            count = 0
            # 并输出
            print result

    file1.close()
