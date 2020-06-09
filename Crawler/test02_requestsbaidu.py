#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: test_requestsbaidu.py
 @time: 2019\4\1 0001 14:43
 @desc:
"""
import requests


url = "http://www.so.com/s"  # http://www.baidu.com/s
keyword = "Python"
try:
    # kv = {'wd':keyword}
    # r = requests.get(url, params=kv)
    kv_360 = {'q':keyword}
    r = requests.get(url, params=kv_360)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.headers)
    print(len(r.text))
except Exception as e:
    print("爬取失败，失败原因：{}".format(e))
