#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 18 August, 2017

import cookielib
import urllib2

filename = 'python_urllib2_6.log'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.sogou.com")

cookie.save(ignore_discard=True, ignore_expires=True)


cookie_2 = cookielib.MozillaCookieJar()

cookie_2.load('python_urllib2_6.log', ignore_discard=True, ignore_expires=True)

req = urllib2.Request("http://www.sogou.com")

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_2))
response = opener.open(req)
print response.read()
