#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 17 March, 2017

import sys

default_encoding = sys.getdefaultencoding()

print "The current default encoding is: ", default_encoding

reload(sys)

sys.setdefaultencoding('utf-8')

default_encoding = sys.getdefaultencoding()

print "The default encoding has been changed to: ", default_encoding

print "sys.stdin.encoding: ", sys.stdin.encoding

