#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 上午11:32
# @Author  : Aries
# @Site    : 
# @File    : py022_crawler.py
# @Software: PyCharm
'''
重构爬虫类
'''
from random import choice
import urllib
import urllib2
import re
import cookielib
import time


class CrawlerBaidu(object):
    '''
    baidu主页爬虫
    '''

    def __init__(self, keyword, ip_list):
        '''
        初始化
        :param keyword: 关键字
        :param ip_list: ip列表
        '''
        headers = {
            'DNT': 1,
            'Host': 'www.baidu.com',
            'Referer': 'http://www.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.headers = headers
        self.keyword = keyword
        self.ip_list = ip_list

    def get_html(self, url):
        '''
        获取html
        :param url: 目标网址
        :return: html string
        '''
        hosturl = 'http://www.baidu.com/'
        ip = choice(self.ip_list)
        try:
            cj = cookielib.LWPCookieJar()
            cookie_support = urllib2.HTTPCookieProcessor(cj)
            proxy_support = urllib2.ProxyHandler({'http': 'http://' + ip})
            opener = urllib2.build_opener(cookie_support, proxy_support, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
            h = urllib.urlopen(hosturl)

            headers = {
                'DNT': 1,
                'Host': 'www.baidu.com',
                'Referer': 'http://www.baidu.com/',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

            }

            req = urllib2.Request(url)
            for key in self.headers:
                req.add_header(key, headers[key])

            r = urllib2.urlopen(req, timeout=50)
            html = r.read()

        except Exception as e:
            print e

        return html

    def get_word(self, html):
        '''
        获取关键字
        :param html: html网页信息
        :return: 返回关键字
        '''
        find_keyword = re.findall(r'rsv_ers=xn1&re_src=0">(.*?)</a>', html)
        return find_keyword


if __name__ == '__main__':

    # test
    keyword_list = ['python', 'golang']
    for line in keyword_list:
        line = urllib.quote(line)

        get_url = 'http://www.baidu.com/s?wd=' + line
        ip_list = [
            '61.155.95.28:8080',
            '60.190.136.90:3128'
        ]

        gather = CrawlerBaidu(line, ip_list)
        out_html = gather.get_html(get_url)
        out_word = gather.get_word(out_html)

        for item in out_word:
            print item

        time.sleep(5)
