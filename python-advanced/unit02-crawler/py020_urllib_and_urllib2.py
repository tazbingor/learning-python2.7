#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 上午10:25
# @Author  : Aries
# @Site    : 
# @File    : py020_urllib_and_urllib2.py
# @Software: PyCharm
'''
urllib 与 urllib2 的区别
   urllib和urllib2均受URL请求的模块,同时也提供了不同的功能
   有以下两个最明显的区别:
        1.urllib2可以接受一个Request类的实例来设置URL请求的headers,urllib只能接收URL.
            也就意味着无法自定义User-Agent等字符串,也就无法设置headers的内容,无法做到反反爬虫
        2.urllib提供urlencode方法用啦GET查询字符的产生,而urllib2没有.所以在使用python爬虫的时候
            会把这两个模块都使用到
'''
import urllib
import urllib2
import re
import cookielib

get_url = 'https://www.baidu.com/s?wd=%E7%A7%91%E6%8A%80&rsv_spt=1&rsv_iqid=0xedac68690000247c&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=1113&rsv_sug4=1113'

headers = {
    'Cookie': 'BAIDUID=8A9A0786EC1853FD72CF74ECD56D91FE:FG=1; BIDUPSID=8A9A0786EC1853FD72CF74ECD56D91FE; PSTM=1477837639; BDSFRCVID=s-tsJeC62Guo1NTA86fLTx8dAeKTppOTH6aodft9U5XBMsxpzgyIEG0PDM8g0KubfeDEogKKLgOTHUQP; H_BDCLCKID_SF=tJPf_I_XtC03jnkkMb7M26oH-UIs2RFL-2Q-5KL-Jpbdq-QOLjA-5hF72a7b34QiJC6w2MbdJJjofqv8h-JG-t5DbarWKPvABmTxoUJgBCnJhhvG-45Ij5_ebPRiWPb9QgbPbxtLtDtabKImjTD3bI60Dqbe5-KXKKOLV-LXfPOkeq8CDxJhhT_N3-LOttKtQT-O0pjHWMb2qh72y5jHhP0E5arPtlvGB67OQPcjMlTpsIJMQMFWbT8U5f5hKx34aKviahRjBMb1SfjMe6K2Djv-jatqq--XJR6eQbODHJOoDDvRqJO5y4LdjG5x-44DBHnCVIQDBUbWbbbqbfRxKb8g3-Aq54Rb5jP8-C590q65J-JubnrzQfbQ0-OuqP-jW5Ta0J5g3R7JOpvsbUnxyhLu0a62btt_JRIeof5; BDUSS=3dNaUZFWUZ5OW5ySXNONm5jT3RJT0NSRTN5eUx3Z1J1RWNGOC1lcXBoUGFlWGxhQVFBQUFBJCQAAAAAAAAAAAEAAAB-sGNVVGF6QmluZ29Fdm8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANrsUVra7FFaS; BD_UPN=123253; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=25710_1453_21090_17001_20928; BD_CK_SAM=1; PSINO=3; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=6a9bjhHh1v%2B0MqPrLpdczEk3%2BzSSIg4ghzV%2BUj9z4%2BhAvT%2F4wHK5KzpFzWKfMx4LdCbr; BDSVRTM=0; pgv_pvi=7747851264; pgv_si=s9004911616',
    'DNT': 1,
    'HOST': 'www.baidu.com',
    'Referer': 'http://www.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'
}
keyword = '科技'
keyword = urllib.quote(keyword)
# print keyword  # %E7%A7%91%E6%8A%80
#
# data = {
#     'wd': '科技',
#     'rsv_spt': 1,
#     'rsv_iqid': 0xedac68690000247c,
#     'issp': 1,
#     'f': 8,
#     'rsv_bp': 0,
#     'rsv_idx': 2,
#     'ie': 'utf - 8',
#     'tn': 'baiduhome_pg',
#     'rsv_enter': 1,
#     'rsv_sug3': 5,
#     'rsv_sug1': 5,
#     'rsv_sug7': 100,
#     'rsv_sug2': 0,
#     'inputT': 1113,
#     'rsv_sug4': 1113,
# }
# data = urllib.urlencode(data)
req = urllib2.Request(get_url)
for key in headers:
    req.add_header(key, headers[key])

r = urllib2.urlopen(req)
html = r.read()
find_keyword = re.findall(r'rsv_ers=xn1&rs_src=0">(.*?)</a>', html)
for item in find_keyword:
    print item
