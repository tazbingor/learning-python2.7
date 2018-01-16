#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/16 上午8:17
# @Author  : Aries
# @Site    : 
# @File    : py012_crawler.py
# @Software: PyCharm
'''
python 爬虫

1.爬虫定义:抓取网页数据的程序

2. 爬虫如何抓取网页数据:
    1.通过每个网页的URL
    2.通过HTML
    3.通过HTTP/HTTPS

3. 爬虫的设计思路:
    1.首先确定爬取网页的URL地址
    2.通过HTTP/HTTP协议来和获取对应的HTML网页
    3.提取HTML页面中的数据:
        a.若是需要的数据,就保存起来
        b.若是页面中的其他url,继续上述的第二步,以此类推

4. python常用的爬虫库
    urllib,urllib2,requests,

5. 抓取HTML
    http请求的处理
    处理后的请求可以模拟浏览器发送请求,获取服务器相应的文件

6. 解析服务器的内容
    re,xpath,beautiful soup 4,jsonpath,pyquery
    匹配页面

7. 常用框架Scrapy
    高性能,搞定制,使用的异步框架
    提供了数据存储,数据下载,提取规则等组件

8. 分布式策略:
    Scrapy-redis,数据临时存储,请求指纹去重,请求分配

9. 网络安全
    爬虫与反爬虫

10. 通用爬虫和聚焦爬虫
    通用爬虫: 搜索引擎用的爬虫系统,尽可能将互联网上所有的网页下载下来,放到本地服务器形成备份,再对这些网页做相关处理
    聚焦爬虫: 针对特定的某种内容的爬虫

11. 爬虫流程
    网页爬取->存储->处理内容->提供检索

使用urllib库获取360搜索主页的信息
'''
import urllib
import urllib2
import re


def get360():
    html = urllib2.urlopen('https://www.so.com/').read()
    return html


def get360Web(keyword=''):
    key = urllib.quote(keyword)
    print keyword
    url = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q=' + key

    headers = {
        'GET': url,
        'Host': 'www.so.com',
        'Referer': 'https://www.so.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    req = urllib2.Request(url)
    # req.add_header('Host', 'http://www.python.org/')  # 追加头
    # req.add_header('Referer', 'http://www.python.org/')  # 追加头
    for key in headers:
        req.add_header(key, headers[key])

    html = urllib2.urlopen(req).read()
    # print html
    re_360 = re.findall("\"([^x00-xff]+?)\"", html)

    return sub_symbol(re_360)


def sub_symbol(str_list=[]):
    new_list = []
    for item in str_list:
        if is_symbol(item):
            new_list.append(item)
    return new_list


def is_symbol(string=''):
    try:
        if re.match(u'[\u4e00-\u9fa5]+', string).group():
            return True
    except AttributeError:
        return False


if __name__ == '__main__':
    # get360()
    for item in get360Web('杜琪峰'):
        print item
