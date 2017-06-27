#!/usr/bin/env python3
# -*- utf-8 -*-
# 2 June, 2017
#
# Karl.Lv@outlook.com, KarlLv@126.com
#
# Python Regular Expression examples

import re

p2 = re.compile(r'万')
str_ch_2 = '2318万'
print(p2.sub(r'0000', str_ch_2))

print('The UNICODE of 万 is:', hex(ord('万')))

p3 = re.compile(r'\u4e07')
str_ch_3 = '293万123万'
print(p3.sub(r'0000', str_ch_3))

str_ch_4 = '28938万万'
if re.findall(r'万', str_ch_4):
    print(re.sub(r'万', '0000', str_ch_4))
