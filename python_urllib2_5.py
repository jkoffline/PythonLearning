#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 August, 2017

import urllib2
import cookielib

cookie = cookielib.CookieJar()

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.sogou.com')

for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
