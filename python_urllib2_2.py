#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# http://python.jobbole.com/81339/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 August, 2017
#

import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.126.com')
