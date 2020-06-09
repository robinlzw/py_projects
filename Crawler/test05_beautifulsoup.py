#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: test_beautifulsoup.py
 @time: 2019\4\1 0001 15:17
 @desc:
"""
import requests
from bs4 import BeautifulSoup


r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, 'lxml')
title = soup.title
tag = soup.a
tag_string = tag.string
a_name = soup.a.name
a_parent_name = soup.a.parent.name
a_parent_parent_name = soup.a.parent.parent.name
a_string = soup.a.string
attrs = tag.attrs
attrs_class = tag.attrs['class']
attrs_href = tag.attrs['href']
attrs_type = type(tag.attrs)
tag_type = type(tag)

print(title, tag, tag_string, a_name, a_parent_name, a_parent_parent_name, a_string, attrs, attrs_class, attrs_href,
      attrs_type, attrs_type, tag_type)
print(soup.prettify())
