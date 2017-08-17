#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')

try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
