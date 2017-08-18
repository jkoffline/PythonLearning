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
