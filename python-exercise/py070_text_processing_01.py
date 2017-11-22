#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午5:46
# @Author  : Aries
# @Site    : 
# @File    : py070_text_processing_01.py
# @Software: PyCharm
'''
8-10.文本处理 统计一句话中的元音,辅音及单词(以空格分割)的个数.忽略元音和辅音的特
    殊情况,如"h","y","qu"等. 附加题:编写处理这些特殊情况的代码.
'''

vowels = ['a', 'e', 'i', 'o', 'u']

def wordCount(myString):
    vowel_count = 0
    consonant_count = 0

    for i in myString:
        if i in vowels:
            vowel_count += 1
        elif i != ' ':
            consonant_count += 1
    word_count = len(str(myString).split())
    return [vowel_count, consonant_count, word_count]


num = raw_input('请输入一段文字:\n')
print '元音数量为：', wordCount(num)[0]
print '辅音数量为：', wordCount(num)[1]
print '单词数量为：', wordCount(num)[2]
