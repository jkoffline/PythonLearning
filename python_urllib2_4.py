#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 August, 2017

import urllib2

request = urllib2.Request('http://www.xxxxxxxx.sh')

try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
