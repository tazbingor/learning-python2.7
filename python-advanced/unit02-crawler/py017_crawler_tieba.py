#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/19 下午9:46
# @Author  : Aries
# @Site    : 
# @File    : py017_crawler_tieba.py
# @Software: PyCharm
'''
爬取贴吧
'''
import urllib
import urllib2


def loadPage(url, filename):
    '''
    根据url发送请求,获取服务器的响应文件
    :param url:需要爬取的地址
    :param filename: 文件名
    :return: 返回抓取的html页面源码
    '''
    print '正在下载中' + filename
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
    }
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html, filename):
    '''
    将HTML写入到本地
    :param html: 服务器响应内容
    :param filename : 文件名
    :return:
    '''
    with  open(filename, 'w') as f:
        f.write(html)


def tiebaSpider(url, beginPage, endPage):
    '''
    贴吧调度器,负责处理每个页面的url
    :param url: 贴吧url前部分
    :param beginPage: 起始页
    :param endPage: 结束页
    :return:
    '''
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        html = loadPage(fullurl, filename)
        # print html
        writePage(html, filename)
        print 'done'


def main():
    kw = raw_input('请输入需要爬取贴吧名:')
    beginPage = int(raw_input('输入起始页面:'))
    endPage = int(raw_input('请输入页数页面:'))
    url = 'http://tieba.baidu.com/f?'
    key = urllib.urlencode({'kw': kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)


if __name__ == '__main__':
    main()
