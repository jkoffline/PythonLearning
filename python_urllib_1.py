#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 March, 2017

import urllib

response = urllib.urlopen('http://www.fishc.com')

html = response.read()
html = html.decode('utf-8')

print(html)
