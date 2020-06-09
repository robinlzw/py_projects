#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: test_requestsjd.py
 @time: 2019/4/1 12:57
 @desc:
"""
import requests


url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except Exception as e:
    print("爬取失败，失败原因：{}".format(e))
