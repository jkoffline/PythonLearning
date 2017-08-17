#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 August, 2017
#

import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')

try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
else:
    print "OK"
