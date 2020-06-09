#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: test_requestspic.py
 @time: 2019/4/1 13:52
 @desc:
"""
import requests
import os


url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = ".//pics//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except Exception as e:
    print("爬取失败，失败原因：{}".format(e))