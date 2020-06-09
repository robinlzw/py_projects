#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: test_beautifulfind.py
 @time: 2019\4\1 0001 15:47
 @desc:
"""
import requests
import re
from bs4 import BeautifulSoup


r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, 'lxml')
findall_ab = soup.find_all(['a', 'b'])
findall_name_attrs = soup.find_all('p', 'course')
findall_id = soup.find_all(id=re.compile('link'))
findall_recursive = soup.find_all('a', recursive=False)
findall_string1 = soup.find_all(string='Basic Python')
findall_string2 = soup.find_all(string=re.compile('python'))

print(findall_ab, findall_name_attrs, findall_id, findall_recursive, findall_string1, findall_string2)
