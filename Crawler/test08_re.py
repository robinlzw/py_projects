#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @author: antenna
 @license: (C) Copyright 2019, Antenna.
 @contact: lilyef2000@gmail.com
 @software:
 @file: test_re.py
 @time: 2019\4\1 0001 17:34
 @desc:
"""
import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print("re.search(): {}, type(match):{}".format(match.group(0), type(match)))

match = re.match(r'[1-9]\d{5}', 'BIT 100081')  # match是从一个字符串的开始位置起匹配正则表达式
if match:
    print("re.match(): {}".format(match.group(0)))

ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print("re.findall(): {}".format(ls))

split = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print("re.split(): {}".format(split))

split = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
print("re.split(maxsplit=1): {}".format(split))

for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print("re.finditer(): {}".format(m.group(0)))

sub = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
print("re.sub():{}".format(sub))

match = re.search(r'[1-9]\d{5}', 'BIT 100081 TSU100084')
if match:
    print("match.string:{}, match.re:{}, match.pos:{}, match.endpos:{}, match.group(0):{}, match.start():{}, match.end():{},\
 match.span():{}".format(match.string, match.re, match.pos, match.endpos, match.group(0), match.start(), match.end(),
                         match.span()))

match = re.search(r'PY.*N', 'PYANBNCNDN')
if match:
    print("贪婪匹配：{}".format(match.group(0)))

match = re.search(r'PY.*?N', 'PYANBNCNDN')
if match:
    print("最小匹配：{}".format(match.group(0)))
"""
*? 前一个字符0次或无限次扩展，最小匹配
+？前一个字符1次或无限次扩展，最小匹配
?? 前一个字符0次或1次扩展，最小匹配
{m,n}? 扩展前一个字符m至n次（含n），最小匹配
"""