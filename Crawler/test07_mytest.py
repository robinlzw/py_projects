#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: mytest.py
 @time: 2019/3/23 21:00
 @desc:
"""

import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return e


def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def print_univ_list(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo, 20)  # 20 univs


main()
